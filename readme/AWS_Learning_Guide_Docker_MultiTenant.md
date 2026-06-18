# AWS Learning Guide: Multi-Tenant Student Project with Docker

## Table of Contents
1. [Project Overview](#project-overview)
2. [AWS Free Services Stack](#aws-free-services-stack)
3. [Docker Installation on Windows](#docker-installation-on-windows)
4. [Local Development Setup](#local-development-setup)
5. [Project Architecture](#project-architecture)
6. [AI Prompt for Project Generation](#ai-prompt-for-project-generation)
7. [Deployment to AWS EC2](#deployment-to-aws-ec2)

---

## PROJECT OVERVIEW

### What We're Building
A **Multi-Tenant Student Learning Management System** with:
- **Agents/Automation**: Automated task assignment, grade calculation, deadline reminders
- **Multi-Tenancy**: Multiple schools/organizations on one system
- **Authentication**: Role-based access (Admin, Teacher, Student)
- **Database**: Persistent data storage
- **Real-world Features**: Course management, assignments, submissions, grading

### Why This Project?
✅ Covers ALL core AWS concepts (compute, database, storage, networking)
✅ Uses only FREE tier services
✅ Real-world architecture (multi-tenancy is industry standard)
✅ Scalable and production-ready mindset
✅ Perfect for portfolio building

---

## AWS FREE SERVICES STACK

### Services We'll Use (All Free Tier Eligible)

| Service | Purpose | Free Tier | Learning Value |
|---------|---------|-----------|-----------------|
| **EC2** | Compute/Servers | 750 hrs/month | Core infrastructure |
| **RDS (MySQL/PostgreSQL)** | Managed Database | 750 hrs/month | Data persistence |
| **S3** | File Storage | 5GB | Document/file uploads |
| **CloudWatch** | Monitoring/Logs | 5GB logs/month | System health |
| **IAM** | Access Control | Unlimited | Security best practice |
| **SQS** | Message Queue | 1M requests/month | Agent/async tasks |
| **Lambda** (Optional) | Serverless Functions | 1M invocations/month | Cost optimization |
| **Route 53** | DNS | 50 queries/month | Domain management |

### What We DON'T Need (Cost-wise)
- ❌ RDS Multi-AZ (use single AZ for learning)
- ❌ Load Balancer (EC2 alone is fine for learning)
- ❌ CloudFront CDN (not needed for this scale)

### Cost Estimate: **$0 - $5/month** (if careful)

---

## DOCKER INSTALLATION ON WINDOWS

### Step 1: System Requirements Check
```
Windows 10/11 (Pro, Enterprise, or Education Edition recommended)
- Home Edition works but with limitations
- At least 4GB RAM (8GB+ recommended)
- Virtualization enabled in BIOS
```

### Step 2: Check Virtualization
1. Press `Ctrl + Shift + Esc` → Open Task Manager
2. Go to **Performance** tab
3. Look for **Virtualization**: Should say "Enabled"
4. If disabled: Restart → Press DEL/F2 → BIOS → Enable Virtualization/VT-x

### Step 3: Install Docker Desktop

**Option A: Official Docker Desktop (Recommended)**
1. Download from: https://www.docker.com/products/docker-desktop
2. Double-click installer → Follow prompts
3. **IMPORTANT**: During installation, ensure "WSL 2" is selected
4. Restart computer when prompted
5. Open PowerShell and verify:
```powershell
docker --version
docker run hello-world
```

**Option B: Docker with WSL 2 (Windows Subsystem for Linux)**
If standard Docker has issues:
1. Open PowerShell as Admin:
```powershell
wsl --install
wsl --install -d Ubuntu
```
2. Restart computer
3. Set Ubuntu as default WSL:
```powershell
wsl --set-default Ubuntu
```
4. Install Docker Desktop (will auto-detect WSL 2)

### Step 4: Create Docker Hub Account
1. Go to https://hub.docker.com
2. Click "Sign Up"
3. Create free account (username will be your Docker ID)
4. Verify email
5. In Docker Desktop → Settings → Sign in with your account
6. Or via PowerShell:
```powershell
docker login
# Enter username and password when prompted
```

### Step 5: Verify Installation
```powershell
docker --version
docker info
docker run hello-world
```

---

## LOCAL DEVELOPMENT SETUP

### Folder Structure for Your Project
```
StudentLMS-Project/
├── backend/
│   ├── app.py (or index.js/main.go)
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
├── database/
│   ├── schema.sql
│   ├── init.sql
│   └── Dockerfile (optional)
├── docker-compose.yml
├── .env
└── README.md
```

### Step 1: Create Project Directory
```powershell
# Open PowerShell or Command Prompt
mkdir StudentLMS-Project
cd StudentLMS-Project
```

### Step 2: Docker Compose File (Local Development)
Create file: `docker-compose.yml`

```yaml
version: '3.8'

services:
  # Database Service
  database:
    image: mysql:8.0
    container_name: lms_db
    environment:
      MYSQL_ROOT_PASSWORD: root_password_123
      MYSQL_DATABASE: student_lms
      MYSQL_USER: lms_user
      MYSQL_PASSWORD: lms_password
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
      - ./database/init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - lms_network
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Backend API Service
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: lms_api
    environment:
      DB_HOST: database
      DB_PORT: 3306
      DB_NAME: student_lms
      DB_USER: lms_user
      DB_PASSWORD: lms_password
      JWT_SECRET: your_jwt_secret_key_change_this
      AWS_REGION: us-east-1
      AWS_ACCESS_KEY_ID: ${AWS_ACCESS_KEY_ID}
      AWS_SECRET_ACCESS_KEY: ${AWS_SECRET_ACCESS_KEY}
    ports:
      - "5000:5000"
    depends_on:
      database:
        condition: service_healthy
    networks:
      - lms_network
    volumes:
      - ./backend:/app
    command: python app.py  # or node index.js, etc

networks:
  lms_network:
    driver: bridge

volumes:
  mysql_data:
    driver: local
```

### Step 3: Create .env File
Create file: `.env`
```
# Don't commit this to git!
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_REGION=us-east-1
DB_ROOT_PASSWORD=root_password_123
DB_USER=lms_user
DB_PASSWORD=lms_password
ENVIRONMENT=local
```

### Step 4: Run Locally
```powershell
# In project directory
docker-compose up --build

# Check if running
docker-compose ps

# View logs
docker-compose logs -f backend

# Stop
docker-compose down
```

---

## PROJECT ARCHITECTURE

### Multi-Tenant Design
```
┌─────────────────────────────────────────┐
│        Load Balancer (Future)           │
└────────────────────┬────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
    ┌───▼────┐              ┌───▼────┐
    │  EC2   │              │  EC2   │
    │Instance│              │Instance│
    │  (API) │              │ (API)  │
    └────┬───┘              └────┬───┘
         │                       │
         └───────────┬───────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
    ┌────▼────┐            ┌────▼────┐
    │   RDS   │            │    S3   │
    │ MySQL   │            │ Storage │
    └─────────┘            └─────────┘
         │
    ┌────▼────┐
    │ CloudWatch/
    │  Logs   │
    └─────────┘
```

### Database Schema (Multi-Tenant)
```sql
-- Tenant table (each school/org)
CREATE TABLE tenants (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    subdomain VARCHAR(100) UNIQUE,
    subscription_plan VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Users table (with tenant isolation)
CREATE TABLE users (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255),
    role ENUM('admin', 'teacher', 'student'),
    created_at TIMESTAMP,
    FOREIGN KEY (tenant_id) REFERENCES tenants(id),
    UNIQUE KEY unique_tenant_email (tenant_id, email)
);

-- Courses
CREATE TABLE courses (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL,
    name VARCHAR(255),
    description TEXT,
    teacher_id UUID NOT NULL,
    created_at TIMESTAMP,
    FOREIGN KEY (tenant_id) REFERENCES tenants(id),
    FOREIGN KEY (teacher_id) REFERENCES users(id)
);

-- Assignments
CREATE TABLE assignments (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL,
    course_id UUID NOT NULL,
    title VARCHAR(255),
    description TEXT,
    due_date DATETIME,
    created_at TIMESTAMP,
    FOREIGN KEY (tenant_id) REFERENCES tenants(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Submissions
CREATE TABLE submissions (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL,
    assignment_id UUID NOT NULL,
    student_id UUID NOT NULL,
    submission_url VARCHAR(500),
    grade INT,
    submitted_at TIMESTAMP,
    FOREIGN KEY (tenant_id) REFERENCES tenants(id),
    FOREIGN KEY (assignment_id) REFERENCES assignments(id),
    FOREIGN KEY (student_id) REFERENCES users(id)
);
```

### Authentication Flow
```
1. Student Login
   ↓
2. Validate Tenant (subdomain)
   ↓
3. Check Credentials (JWT)
   ↓
4. Return Auth Token with tenant_id
   ↓
5. All API requests include Authorization header
   ↓
6. Middleware validates token + tenant_id
```

### Agents/Automation Examples
```
1. Task Agent
   - Runs every hour
   - Sends reminders for due assignments
   - Marks late submissions

2. Grading Agent
   - Auto-calculates grades from rubrics
   - Detects plagiarism

3. Notification Agent
   - Emails users on grade updates
   - Slack/SMS notifications (future)
```

---

## AI PROMPT FOR PROJECT GENERATION

Use this prompt with Claude/Anthropic to generate your project:

### PROMPT TO GIVE TO CLAUDE:

```
You are an expert full-stack developer creating a production-ready multi-tenant 
Student Learning Management System (LMS) as an educational project.

## REQUIREMENTS:

### Tech Stack
- Backend: [Choose: Python (Flask/FastAPI), Node.js (Express), or Go (Gin)]
- Frontend: React.js (optional for initial phase)
- Database: MySQL/PostgreSQL
- Authentication: JWT with role-based access control (RBAC)
- File Storage: AWS S3 integration
- Deployment: Docker containers on AWS EC2

### Core Features

1. **Multi-Tenancy**
   - Each school/organization is a separate tenant
   - Tenant isolation at database level (tenant_id in all tables)
   - Subdomain-based tenant identification (school1.lms.com, school2.lms.com)
   - Tenant admin dashboard

2. **Authentication & Authorization**
   - JWT-based authentication
   - Roles: Admin (tenant level), Teacher, Student
   - Endpoints:
     - POST /auth/register (with email verification)
     - POST /auth/login (returns JWT token)
     - POST /auth/refresh-token
     - GET /auth/me (current user info)
   - Middleware to validate tenant + user permissions

3. **Core Business Logic**
   - Courses: Create, read, update, delete courses
   - Assignments: Create, update, set deadlines
   - Submissions: Students submit work (file or text)
   - Grading: Teachers grade submissions
   - Attendance: Track student attendance (optional)

4. **Database Schema**
   - tenants table (organizations)
   - users table (with tenant_id, role)
   - courses table (with teacher_id)
   - assignments table (with due_date)
   - submissions table (with grade)
   - audit_logs table (for compliance)

5. **APIs Required**
   - Authentication endpoints (register, login, logout, refresh)
   - Course CRUD + enrollment
   - Assignment CRUD + search
   - Submission upload/download with S3
   - Grade management
   - User management (admin only)
   - Tenant settings (admin only)

6. **AWS Integration**
   - S3 for file uploads/downloads
   - RDS for MySQL database
   - IAM roles for EC2 instances
   - CloudWatch for logging and monitoring
   - (Optional) SQS for async task processing
   - (Optional) Lambda for scheduled agents

7. **Agents/Automation** (Scheduled Tasks)
   - Assignment Reminder Agent: Daily check for upcoming/overdue assignments
   - Auto-Grading Agent: Calculate grades based on rubrics
   - Notification Agent: Send emails on submission/grade updates
   - Cleanup Agent: Archive old courses/submissions

8. **Error Handling & Logging**
   - Structured logging (JSON format)
   - Error responses with proper HTTP status codes
   - Request/response logging for debugging
   - Exception handling with detailed stack traces

9. **Validation & Security**
   - Input validation on all endpoints
   - CORS enabled for frontend
   - Rate limiting on auth endpoints
   - Password hashing (bcrypt)
   - SQL injection prevention (parameterized queries)
   - HTTPS ready configuration

10. **Configuration**
    - Environment variables (.env file)
    - Separate configs for local, staging, production
    - Database connection pooling

## DELIVERABLES:

1. **Backend API** with all endpoints above
2. **Dockerfile** for containerization
3. **docker-compose.yml** for local development (with MySQL)
4. **Database schema** (SQL migration files)
5. **README.md** with:
   - Setup instructions
   - API documentation
   - Testing guide
   - Deployment steps
6. **Example .env file** with all required variables
7. **Basic test cases** (Postman collection or cURL examples)

## CONSTRAINTS:
- Code should be clean, well-commented, and production-ready
- Follow [chosen language] best practices
- Implement proper error handling throughout
- Use environment variables for all configurations
- No hardcoded credentials
- Include input validation and sanitization
- Add request/response logging

Generate the complete, working project structure and code. The code should be 
ready to run with `docker-compose up` in local environment.
```

---

## DEPLOYMENT TO AWS EC2

### Step 1: AWS Account Setup (Free Tier)
1. Go to https://aws.amazon.com/free/
2. Click "Create a Free Account"
3. Complete registration and payment method (won't charge for free tier)
4. Wait for account activation (usually instant)

### Step 2: Create EC2 Instance
```
1. Go to AWS Console → EC2 → Instances → Launch Instance

2. Choose AMI:
   - Ubuntu Server 22.04 LTS (Free tier eligible)

3. Instance Type:
   - t2.micro (1 vCPU, 1GB RAM, free)

4. Key Pair:
   - Create new key pair: "lms-project.pem"
   - Download and SAVE SECURELY

5. Network Settings:
   - Create new security group OR use default
   - Add inbound rules:
     * SSH (port 22) - from your IP
     * HTTP (port 80) - from anywhere
     * HTTPS (port 443) - from anywhere
     * Custom (port 5000) - from anywhere (for API)

6. Storage:
   - Keep 30GB (free tier allows 30GB)

7. Launch Instance

8. Wait for instance to show "Running" status
```

### Step 3: Connect to EC2 Instance
```powershell
# Open PowerShell and navigate to where you saved the .pem file
# On Windows, you may need to use PuTTY or Windows Terminal with WSL

# Via WSL (if you have WSL2):
cd /mnt/c/path/to/pem/file
chmod 400 lms-project.pem
ssh -i lms-project.pem ubuntu@your-instance-public-ip

# Or find IP in AWS Console → Instances → Your instance → Public IPv4 address
```

### Step 4: Install Docker on EC2
```bash
# Once connected to EC2

# Update system
sudo apt update
sudo apt upgrade -y

# Install Docker
sudo apt install docker.io -y

# Add ubuntu user to docker group
sudo usermod -aG docker ubuntu

# Verify installation
docker --version

# Exit and reconnect for user group to take effect
exit
# SSH back in
```

### Step 5: Upload Your Project
```powershell
# From your Windows PowerShell
# Copy entire project to EC2
scp -i lms-project.pem -r C:\Path\To\StudentLMS-Project ubuntu@your-instance-ip:/home/ubuntu/

# SSH back in and verify
ssh -i lms-project.pem ubuntu@your-instance-ip
cd StudentLMS-Project
```

### Step 6: Create RDS Database (AWS Managed)
```
1. Go to AWS Console → RDS → Create Database
2. Choose MySQL 8.0 (free tier eligible)
3. DB Instance ID: student-lms-db
4. Username: lms_user
5. Password: (Create strong password)
6. DB Instance Class: db.t2.micro (free)
7. Storage: 20GB (free tier)
8. Publicly accessible: Yes (for learning, set to No in production)
9. Database name: student_lms
10. Skip backup for learning phase
11. Create Database
12. Wait for status to show "Available"
13. Get endpoint from Details page
```

### Step 7: Setup on EC2 with RDS
```bash
# SSH into EC2

# Update environment variables
cd StudentLMS-Project
nano .env

# Update with RDS values:
DB_HOST=your-rds-endpoint.rds.amazonaws.com
DB_PORT=3306
DB_NAME=student_lms
DB_USER=lms_user
DB_PASSWORD=your_rds_password
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
ENVIRONMENT=production

# Save (Ctrl+X, Y, Enter)

# Update docker-compose.yml to remove local database service
# Or create a production docker-compose file without DB service
```

### Step 8: Deploy with Docker
```bash
# Still in project directory on EC2

# Build image
docker build -t student-lms:latest ./backend

# Run container
docker run -d \
  --name lms-api \
  -p 5000:5000 \
  --env-file .env \
  student-lms:latest

# Check if running
docker ps

# View logs
docker logs -f lms-api
```

### Step 9: Access Your Application
```
Find your EC2 Public IP from AWS Console
Open browser: http://your-ec2-public-ip:5000
```

### Step 10: Setup Domain (Optional with Route 53)
```
1. Register domain or use existing
2. AWS Route 53 → Hosted Zones → Create Hosted Zone
3. Add domain
4. Create A record pointing to EC2 Elastic IP
5. Update name servers in domain registrar
6. Wait for DNS propagation (can take 24-48 hours)
```

---

## MONITORING & MAINTENANCE

### View EC2 Logs
```bash
# SSH to instance
docker logs lms-api

# View system metrics
htop

# Check disk space
df -h

# Check network
netstat -tulnp
```

### CloudWatch Integration
```
1. EC2 instance automatically sends metrics
2. Go to AWS Console → CloudWatch → Dashboards
3. Create dashboard to monitor:
   - CPU usage
   - Memory usage
   - Network traffic
   - API response times
```

### Backup Strategy
```bash
# Create RDS snapshots regularly
# Go to RDS Console → Snapshots → Create Snapshot

# Or use AWS Backup Service for automated backups
```

---

## COST MANAGEMENT CHECKLIST

✅ Use t2.micro for EC2 (free 750 hours/month)
✅ Use db.t2.micro for RDS (free 750 hours/month)
✅ Stop instances when not using (nights/weekends)
✅ Set up AWS Budget alerts (email if > $5/month)
✅ Remove unused resources immediately
✅ Use S3 Standard (not Glacier for this project)
✅ Limit outbound data transfer (free tier: 100GB)

### Check Free Tier Usage
```
AWS Console → Billing → Free Tier Usage
Monitor monthly to stay within limits
```

---

## NEXT STEPS

1. **Week 1-2**: Install Docker, set up local environment
2. **Week 2-4**: Get project generated, test locally
3. **Week 4-5**: Create AWS account, understand services
4. **Week 5-6**: Deploy to EC2 and RDS
5. **Week 6-8**: Optimize, add monitoring, document

---

## USEFUL COMMANDS REFERENCE

### Docker Commands
```powershell
# Build image
docker build -t myimage:tag .

# Run container
docker run -d --name mycontainer myimage:tag

# Stop container
docker stop mycontainer

# View logs
docker logs -f mycontainer

# Remove container
docker rm mycontainer

# See all containers
docker ps -a

# See all images
docker images
```

### Docker Compose Commands
```powershell
# Start all services
docker-compose up -d

# Rebuild and start
docker-compose up -d --build

# Stop all services
docker-compose down

# View logs
docker-compose logs -f service-name

# Execute command in running container
docker-compose exec service-name bash
```

### AWS CLI Commands
```bash
# List EC2 instances
aws ec2 describe-instances

# List RDS databases
aws rds describe-db-instances

# List S3 buckets
aws s3 ls

# Upload file to S3
aws s3 cp file.txt s3://bucket-name/

# Download from S3
aws s3 cp s3://bucket-name/file.txt .
```

---

## TROUBLESHOOTING

### Docker won't start on Windows
- Check Virtualization is enabled in BIOS
- Ensure WSL 2 is installed
- Restart Docker Desktop from system tray

### Can't connect to RDS from EC2
- Check security group allows port 3306
- Verify RDS is publicly accessible
- Test connection with: `mysql -h endpoint -u user -p`

### Container exits immediately
- Check logs: `docker logs container-name`
- Verify environment variables are set
- Check database connectivity

### Cost exceeding free tier
- Stop unused EC2 instances
- Delete old RDS snapshots
- Check for data transfer charges
- Review CloudWatch logs for errors

