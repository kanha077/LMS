# AWS Learning Project - Quick Reference & Practical Checklists

## SECTION 1: WINDOWS DOCKER SETUP - QUICK COMMANDS

### Initial Setup (First Time Only)
```powershell
# 1. Download Docker Desktop
# Go to: https://www.docker.com/products/docker-desktop
# Run installer, restart computer

# 2. Verify installation
docker --version
docker run hello-world

# 3. Create Docker Hub account
# https://hub.docker.com/signup
# Then login
docker login
# Enter username and password

# 4. Create project folder
mkdir C:\Projects\StudentLMS
cd C:\Projects\StudentLMS

# 5. Create .env file (Windows PowerShell)
notepad .env
# Paste content:
# DB_HOST=database
# DB_PASSWORD=secure_password
# etc.
```

### Everyday Docker Commands (Windows PowerShell)
```powershell
# Navigate to project
cd C:\Projects\StudentLMS

# Start all containers
docker-compose up -d

# View running containers
docker-compose ps

# View logs (follow in real-time)
docker-compose logs -f backend

# Stop all containers
docker-compose down

# View specific service logs
docker-compose logs backend

# Restart a service
docker-compose restart backend

# Execute command in running container
docker-compose exec backend bash
# Then inside container:
# python -m pytest
# pip install package_name
# etc.

# Remove all containers and volumes (CAREFUL!)
docker-compose down -v

# Rebuild after code changes
docker-compose up -d --build
```

### Troubleshooting Docker on Windows
```powershell
# Docker daemon not starting?
# Open PowerShell as Admin:
Restart-Service com.docker.service

# WSL2 not working?
wsl --list --verbose
wsl --set-default-version 2

# Out of disk space?
docker system prune -a
docker volume prune

# Check Docker resource usage
docker stats

# View Docker system info
docker system df
```

---

## SECTION 2: DATABASE OPERATIONS

### MySQL Operations (From Windows or Inside Container)

#### Option A: Using Windows MySQL Client
```powershell
# Install MySQL client (if not already installed)
# https://dev.mysql.com/downloads/mysql/

# Connect to local database
mysql -h localhost -P 3306 -u lms_user -p
# Password: lms_password

# Common commands inside MySQL:
SHOW DATABASES;
USE student_lms;
SHOW TABLES;
SELECT * FROM users;
DESC users;  -- Show table structure
```

#### Option B: Using Docker
```powershell
# Access MySQL inside container
docker-compose exec database mysql -u lms_user -p student_lms
# Password: lms_password

# Or as root
docker-compose exec database mysql -u root -p
# Password: root_password_123
```

#### Backup Database
```bash
# Backup entire database
docker-compose exec database mysqldump -u lms_user -p student_lms > backup.sql

# Restore from backup
docker-compose exec -T database mysql -u lms_user -p student_lms < backup.sql

# On Windows, may need to redirect differently:
docker-compose exec database mysqldump -u root -p root_password_123 > backup.sql
```

### View Database Schema
```sql
-- Show all tables
SHOW TABLES;

-- Show table structure
DESCRIBE users;
DESCRIBE courses;

-- Count records
SELECT COUNT(*) FROM users;
SELECT COUNT(*) FROM courses;
SELECT COUNT(*) FROM submissions;

-- Sample data
SELECT id, email, role FROM users LIMIT 10;
SELECT * FROM courses WHERE tenant_id = 'your-tenant-id';
```

---

## SECTION 3: AWS ACCOUNT SETUP CHECKLIST

### Week 1 Checklist: Get Ready
- [ ] Create AWS account at aws.amazon.com/free
- [ ] Verify email
- [ ] Add payment method (won't be charged for free tier)
- [ ] Enable MFA (optional but recommended)
- [ ] Visit AWS Console and familiarize yourself
- [ ] Set up billing alert
  - Go to: Billing & Cost Management → Budgets → Create Budget
  - Set alert for $5/month
  - Gets email if exceeded

### Week 2 Checklist: Create Resources
- [ ] Create EC2 instance (t2.micro)
  - Region: us-east-1 (cheapest)
  - OS: Ubuntu 22.04 LTS
  - Download key pair (.pem file)
  - Save key pair in safe location
- [ ] Create RDS instance (MySQL, db.t2.micro)
  - Write down endpoint
  - Write down username/password
  - Make it publicly accessible (for learning)
- [ ] Create S3 bucket
  - Name: studentlms-uploads-unique-name
  - Block public access initially
- [ ] Create IAM user for application
  - Create access key and secret
  - Attach policy: AmazonS3FullAccess, RDSFullAccess
  - Save credentials

### Week 3 Checklist: Security Setup
- [ ] Create security group for EC2
  - Allow SSH from your IP only
  - Allow HTTP from anywhere
  - Allow HTTPS from anywhere
  - Allow custom port 5000 from anywhere
- [ ] Test SSH connection to EC2
- [ ] Verify EC2 can connect to RDS
  - SSH to EC2
  - Try: `mysql -h rds-endpoint -u user -p`

---

## SECTION 4: LOCAL DEVELOPMENT WORKFLOW

### Daily Workflow Steps

#### 1. Start Development Environment
```powershell
cd C:\Projects\StudentLMS

# Start containers
docker-compose up -d --build

# Wait for services to be healthy
docker-compose ps
# All should show "Up" status

# View logs to confirm
docker-compose logs -f

# Press Ctrl+C to stop viewing logs (containers still running)
```

#### 2. Work on Code
```
Edit files in:
- backend/app/main.py
- backend/app/routes/
- backend/app/services/
etc.

Changes auto-reload due to --reload flag in docker-compose
```

#### 3. Test API Endpoints
```powershell
# Using curl (built into PowerShell)

# Health check
curl http://localhost:5000/api/v1/health

# Register new user
$body = @{
    email = "student@example.com"
    password = "SecurePass123!"
    full_name = "John Student"
    role = "student"
} | ConvertTo-Json

curl -Method POST -Uri http://localhost:5000/api/v1/auth/register `
  -Headers @{"Content-Type" = "application/json"} `
  -Body $body

# Or use Postman (download free desktop app)
```

#### 4. Run Tests
```bash
# Access container
docker-compose exec backend bash

# Inside container, run tests
pytest -v

# With coverage
pytest --cov=app --cov-report=html

# Run specific test
pytest app/tests/test_auth.py -v
```

#### 5. View Logs
```powershell
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f database

# Last 50 lines
docker-compose logs --tail=50 backend

# With timestamps
docker-compose logs -f -t backend
```

#### 6. Stop Development
```powershell
# Stop containers (keeps data)
docker-compose stop

# Or down (removes containers)
docker-compose down

# Remove volumes (DELETE ALL DATA)
docker-compose down -v
```

---

## SECTION 5: GIT WORKFLOW

### Initialize Git Repository
```powershell
cd C:\Projects\StudentLMS

# Initialize git
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Create .gitignore
notepad .gitignore
```

### .gitignore Content
```
# Environment variables
.env
.env.local
.env.*.local

# Docker
.dockerignore

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Database
*.db
*.sqlite
*.sqlite3
database.sql
backup.sql

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Testing
.pytest_cache/
htmlcov/
.coverage

# Logs
logs/
*.log

# AWS
aws_credentials
```

### Git Workflow
```powershell
# Check status
git status

# Add files
git add .

# Commit
git commit -m "Initial project setup"

# Create GitHub repo and push
# Create repo at https://github.com/new
# Then:
git remote add origin https://github.com/YOUR_USERNAME/StudentLMS.git
git branch -M main
git push -u origin main

# Future pushes
git push
```

---

## SECTION 6: AWS DEPLOYMENT QUICK STEPS

### Launch EC2 Instance (Step-by-Step)

```
1. AWS Console → EC2 → Instances
2. Click "Launch instances"
3. Choose: Ubuntu Server 22.04 LTS
4. Instance type: t2.micro
5. Key pair: Create new → download .pem file → SAVE IT!
6. Network: Default VPC
7. Security group: Create new
   - SSH: Source = My IP
   - HTTP: Source = 0.0.0.0/0
   - HTTPS: Source = 0.0.0.0/0
   - Custom (5000): Source = 0.0.0.0/0
8. Storage: 30GB (default)
9. Click "Launch"
10. Wait for status "Running"
11. Copy Public IPv4 address
```

### Connect to EC2 via SSH
```powershell
# On Windows, in PowerShell

# Navigate to where .pem file is saved
cd C:\Users\YourName\Downloads

# Connect
ssh -i lms-project.pem ubuntu@YOUR_EC2_PUBLIC_IP

# First time will ask "Are you sure?" → type "yes"

# You should now be inside EC2
# Prompt will show: ubuntu@ip-xxx-xxx-xxx-xxx:~$
```

### Install Docker on EC2
```bash
# Once connected via SSH to EC2

# Update system
sudo apt update
sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker ubuntu

# Exit and reconnect
exit

# SSH back in
ssh -i lms-project.pem ubuntu@YOUR_EC2_PUBLIC_IP

# Verify
docker --version
```

### Deploy Project to EC2
```bash
# Option 1: Clone from GitHub (recommended)
git clone https://github.com/YOUR_USERNAME/StudentLMS.git
cd StudentLMS

# Option 2: Copy from Windows
# From Windows PowerShell:
scp -i C:\path\to\lms-project.pem -r C:\Projects\StudentLMS ubuntu@YOUR_EC2_PUBLIC_IP:/home/ubuntu/

# Then on EC2:
cd StudentLMS

# Create .env with AWS values
nano .env
# Update with RDS endpoint, AWS keys, etc.

# Start containers
docker-compose up -d --build

# Check status
docker-compose ps

# View logs
docker-compose logs -f backend
```

### Test Deployment
```bash
# From EC2, test local
curl http://localhost:5000/api/v1/health

# From Windows, test remote
curl http://YOUR_EC2_PUBLIC_IP:5000/api/v1/health

# Access in browser
# http://YOUR_EC2_PUBLIC_IP:5000/api/v1/docs
# (FastAPI automatic API documentation)
```

### Monitor EC2
```bash
# Check running containers
docker ps

# View logs
docker logs -f container_name

# Check disk space
df -h

# Check memory/CPU
top
# Press 'q' to exit

# Check network
netstat -tulnp

# Restart service
docker-compose restart backend
```

---

## SECTION 7: COST MONITORING

### Check Free Tier Usage (AWS Console)
```
1. AWS Console → Billing & Cost Management
2. Left sidebar → Free Tier Usage
3. Monitor:
   - EC2 running hours
   - RDS running hours
   - Data transfer (GB)
   - S3 storage (GB)
```

### Set Up Cost Alert
```
1. AWS Console → Billing & Cost Management → Budgets
2. Create Budget
3. Type: Cost budget
4. Period: Monthly
5. Budgeted amount: $5
6. Email alert if exceeds 100%
```

### Stop Unused Resources
```powershell
# To save costs when not using:

# Stop EC2 (keeps data, can restart)
# AWS Console → EC2 → Instances → Right-click → Instance State → Stop
# Cost: $0 while stopped (but storage still costs)

# Stop RDS
# AWS Console → RDS → Databases → Right-click → Stop
# Cost: $0 while stopped (for 7 days max)

# Keep S3 bucket running (cheap)
```

### Free Tier Limits to Watch
```
EC2:
- t2.micro: 750 hours/month (24/7 for 31 days)
- If you use 2 instances: 375 hours each

RDS:
- db.t2.micro: 750 hours/month
- 20GB storage per month

Data Transfer:
- 100GB outbound per month (free)
- Inbound is free
- Dangerous: If you do a lot of file downloads, can exceed

S3:
- 5GB storage free
- PUT/GET requests are mostly free
```

---

## SECTION 8: TROUBLESHOOTING GUIDE

### Docker Issues

**Problem: "Docker daemon is not running"**
```powershell
# Solution 1: Restart Docker
# Click Docker icon in system tray → Restart

# Solution 2: Restart via PowerShell
Restart-Service com.docker.service

# Solution 3: Reinstall
# Uninstall Docker Desktop
# Delete C:\Program Files\Docker
# Reinstall from docker.com
```

**Problem: "Cannot connect to database"**
```bash
# Check if database container is running
docker-compose ps

# Check database logs
docker-compose logs database

# Try manual connection
docker-compose exec database mysql -u root -p
# If this works, issue is with application connection string

# Check .env file
cat .env
# Verify DB_HOST=database (for docker)
# Verify DB_HOST=localhost (for Windows host)
```

**Problem: "Port already in use"**
```powershell
# Port 5000 is in use by another application

# Find what's using port 5000
netstat -ano | findstr :5000

# Kill process (replace PID with actual number)
taskkill /PID 12345 /F

# Or change port in docker-compose.yml
# Change: "5000:5000" to "5001:5000"
```

### AWS Issues

**Problem: "Cannot SSH to EC2"**
```
1. Check key pair file has correct permissions
2. Check security group allows port 22 from your IP
3. Wait 2-3 minutes after launching instance
4. Check EC2 status checks are green
5. Copy public IP correctly (not private IP)
```

**Problem: "EC2 can't connect to RDS"**
```bash
# SSH to EC2 and test
mysql -h your-rds-endpoint.rds.amazonaws.com -u lms_user -p student_lms

# If can't connect:
1. Check RDS status is "Available"
2. Check RDS security group allows port 3306
3. Check RDS is "Publicly accessible" (for learning)
4. Check password is correct
5. Check RDS endpoint is correct (look it up again)
```

**Problem: "Application logs show permission denied for S3"**
```
1. Check IAM user has S3 access policy
2. Check AWS credentials in .env are correct
3. Check bucket name in .env matches actual bucket
4. Check bucket exists in same region as EC2
```

---

## SECTION 9: PERFORMANCE TIPS

### Database Optimization
```sql
-- Add indexes on frequently searched columns
CREATE INDEX idx_tenant_email ON users(tenant_id, email);
CREATE INDEX idx_course_tenant ON courses(tenant_id);
CREATE INDEX idx_submission_date ON submissions(submitted_at);

-- Check query performance
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';

-- Monitor slow queries
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 2;
```

### Docker Optimization
```powershell
# Remove unused images
docker image prune -a

# Remove unused volumes
docker volume prune

# Limit container memory
# In docker-compose.yml:
# services:
#   backend:
#     mem_limit: 512m
#     cpus: '0.5'
```

### API Optimization
```
1. Add response caching for GET requests
2. Use pagination (limit 20-50 per page)
3. Only fetch required fields
4. Index database columns
5. Use connection pooling
6. Monitor response times with CloudWatch
```

---

## SECTION 10: USEFUL RESOURCES

### Docker
- Documentation: https://docs.docker.com/
- Docker Hub: https://hub.docker.com/
- Docker Best Practices: https://docs.docker.com/develop/dev-best-practices/

### AWS
- Free Tier: https://aws.amazon.com/free/
- EC2 Documentation: https://docs.aws.amazon.com/ec2/
- RDS Documentation: https://docs.aws.amazon.com/rds/
- S3 Documentation: https://docs.aws.amazon.com/s3/
- IAM Documentation: https://docs.aws.amazon.com/iam/
- CloudWatch: https://docs.aws.amazon.com/cloudwatch/

### Python/FastAPI
- FastAPI: https://fastapi.tiangolo.com/
- SQLAlchemy: https://docs.sqlalchemy.org/
- Pydantic: https://docs.pydantic.dev/
- Uvicorn: https://www.uvicorn.org/

### Testing
- Pytest: https://docs.pytest.org/
- Postman: https://www.postman.com/
- Curl: https://curl.se/

### Git/GitHub
- GitHub: https://github.com/
- GitHub Learning Lab: https://github.blog/2020-02-27-introducing-github-learning-lab/
- Markdown Guide: https://www.markdownguide.org/

---

## FINAL CHECKLIST BEFORE DEPLOYMENT

### Code Quality
- [ ] All endpoints tested locally
- [ ] No hardcoded credentials
- [ ] Error handling implemented
- [ ] Logging configured
- [ ] Input validation added
- [ ] Security checks in place

### Docker
- [ ] Docker image builds successfully
- [ ] Containers start without errors
- [ ] Healthchecks working
- [ ] Volumes properly configured
- [ ] Environment variables working

### Database
- [ ] Schema created and tested
- [ ] Indexes added
- [ ] Test data inserted
- [ ] Backup working
- [ ] Can connect from EC2

### AWS Resources
- [ ] EC2 instance running
- [ ] RDS database available
- [ ] S3 bucket created
- [ ] Security groups configured
- [ ] IAM user created with permissions
- [ ] Cost monitoring set up

### Documentation
- [ ] README.md complete
- [ ] API documentation added
- [ ] Setup instructions clear
- [ ] Deployment steps documented
- [ ] Troubleshooting guide included

### Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual API testing done
- [ ] Local docker-compose test complete
- [ ] EC2 deployment test complete

