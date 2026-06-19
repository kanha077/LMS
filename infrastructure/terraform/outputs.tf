output "backend_public_ip" {
  description = "The public IP address of the backend EC2 server"
  value       = aws_instance.lms_backend_server.public_ip
}

output "frontend_s3_website_url" {
  description = "The URL of the S3 static website hosting"
  value       = aws_s3_bucket_website_configuration.lms_frontend_website.website_endpoint
}
