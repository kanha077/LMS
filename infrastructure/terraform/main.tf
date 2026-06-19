terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# --- VPC & Networking ---

resource "aws_vpc" "lms_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "lms-vpc"
  }
}

resource "aws_internet_gateway" "lms_igw" {
  vpc_id = aws_vpc.lms_vpc.id

  tags = {
    Name = "lms-igw"
  }
}

resource "aws_subnet" "lms_public_subnet" {
  vpc_id                  = aws_vpc.lms_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "${var.aws_region}a"

  tags = {
    Name = "lms-public-subnet"
  }
}

resource "aws_route_table" "lms_public_rt" {
  vpc_id = aws_vpc.lms_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.lms_igw.id
  }

  tags = {
    Name = "lms-public-rt"
  }
}

resource "aws_route_table_association" "lms_public_rta" {
  subnet_id      = aws_subnet.lms_public_subnet.id
  route_table_id = aws_route_table.lms_public_rt.id
}

# --- Security Groups ---

resource "aws_security_group" "lms_backend_sg" {
  name        = "lms-backend-sg"
  description = "Allow HTTP, HTTPS, and SSH traffic"
  vpc_id      = aws_vpc.lms_vpc.id

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Backend API"
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "lms-backend-sg"
  }
}

# --- SSH Key Pair ---

resource "tls_private_key" "lms_ssh_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "lms_key_pair" {
  key_name   = "lms-terraform-key"
  public_key = tls_private_key.lms_ssh_key.public_key_openssh
}

resource "local_file" "private_key" {
  content         = tls_private_key.lms_ssh_key.private_key_pem
  filename        = "${path.module}/lms-terraform-key.pem"
  file_permission = "0400"
}

# --- EC2 Instance (Backend + DB) ---

data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "lms_backend_server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  subnet_id     = aws_subnet.lms_public_subnet.id

  vpc_security_group_ids = [aws_security_group.lms_backend_sg.id]
  key_name               = aws_key_pair.lms_key_pair.key_name

  tags = {
    Name = "lms-backend-server"
  }
}

# --- S3 Bucket for Frontend ---

resource "random_id" "bucket_id" {
  byte_length = 8
}

resource "aws_s3_bucket" "lms_frontend_bucket" {
  bucket = "lms-frontend-vue-${random_id.bucket_id.hex}"

  tags = {
    Name = "lms-frontend-bucket"
  }
}

resource "aws_s3_bucket_website_configuration" "lms_frontend_website" {
  bucket = aws_s3_bucket.lms_frontend_bucket.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "index.html" # Vue router fallback
  }
}

resource "aws_s3_bucket_public_access_block" "lms_frontend_public_access" {
  bucket = aws_s3_bucket.lms_frontend_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_policy" "lms_frontend_policy" {
  bucket = aws_s3_bucket.lms_frontend_bucket.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "PublicReadGetObject"
        Effect    = "Allow"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.lms_frontend_bucket.arn}/*"
      },
    ]
  })
  depends_on = [aws_s3_bucket_public_access_block.lms_frontend_public_access]
}
