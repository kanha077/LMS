# AWS Multi-Tenant LMS Project - Generation Prompts & Technical Guides

## PART 1: TECHNOLOGY CHOICE GUIDE

### Choose Your Backend Language

#### Option A: Python (FastAPI) - RECOMMENDED FOR LEARNING
**Pros:**
- Easiest to learn
- Great for rapid development
- Excellent documentation
- Perfect for data/ML integration (future)
- Built-in testing support

**Cons:**
- Slightly slower than Go/Node
- Requires Python knowledge

**Best for:** Students learning, rapid prototyping

---

#### Option B: Node.js (Express)
**Pros:**
- JavaScript (easy to learn)
- Great for JavaScript full-stack
- Large ecosystem (npm)
- Good performance

**Cons:**
- Callback/async complexity
- Less suitable for data-heavy operations

**Best for:** JavaScript developers, full-stack JavaScript

---

#### Option C: Go (Gin)
**Pros:**
- Best performance
- Concurrency built-in
- Great for microservices
- Production-ready from day 1

**Cons:**
- Steeper learning curve
- Verbose compared to Python
- Smaller ecosystem

**Best for:** Performance-critical systems, Go enthusiasts

---

### Recommendation for This Project
**Use Python with FastAPI**
- Easiest to understand for students
- AWS integration libraries are mature
- Great for building agents/scheduled tasks
- Excellent documentation and tutorials

---

## PART 2: EXACT PROMPT FOR CLAUDE/ANTHROPIC

### Copy this entire prompt and give it to Claude:

```
SYSTEM CONTEXT:
You are an expert backend architect creating a production-grade Multi-Tenant 
Student Learning Management System (LMS). This is an educational project that 
will be deployed on AWS. Code must be:
- Clean, well-documented, and follows best practices
- Ready to run immediately with docker-compose
- Secure (JWT auth, input validation, SQL injection prevention)
- Scalable (multi-tenant architecture)
- AWS-ready (S3 integration, environment variables)

================================================================================

PROJECT SPECIFICATION:

## BACKEND FRAMEWORK: Python 3.9+ with FastAPI

## SCOPE:
Create a complete, working backend API with database schema, authentication, 
and core business logic. NO frontend required for this phase.

## ARCHITECTURE REQUIREMENTS:

### 1. Multi-Tenancy Design
- Every data table must have 'tenant_id' column
- Users can only access data from their tenant
- Tenant identified by subdomain (school1.lms.com, school2.lms.com)
- Tenant validation in middleware for every request

### 2. Database Schema (PostgreSQL/MySQL)

```sql
-- Tenants (Organizations/Schools)
CREATE TABLE tenants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    subdomain VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255),
    subscription_plan VARCHAR(50) DEFAULT 'free',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Users (Admin, Teachers, Students)
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    role ENUM('admin', 'teacher', 'student') DEFAULT 'student',
    is_active BOOLEAN DEFAULT TRUE,
    email_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(tenant_id, email),
    INDEX idx_tenant_email (tenant_id, email)
);

-- Courses
CREATE TABLE courses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    code VARCHAR(50) NOT NULL,
    teacher_id UUID NOT NULL REFERENCES users(id),
    semester VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(tenant_id, code),
    INDEX idx_tenant_teacher (tenant_id, teacher_id)
);

-- Course Enrollments (Students in Courses)
CREATE TABLE course_enrollments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    course_id UUID NOT NULL REFERENCES courses(id),
    student_id UUID NOT NULL REFERENCES users(id),
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    grade VARCHAR(2),
    status ENUM('active', 'dropped', 'completed') DEFAULT 'active',
    UNIQUE(tenant_id, course_id, student_id),
    INDEX idx_tenant_course_student (tenant_id, course_id, student_id)
);

-- Assignments
CREATE TABLE assignments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    course_id UUID NOT NULL REFERENCES courses(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    instructions TEXT,
    due_date DATETIME NOT NULL,
    total_points INT DEFAULT 100,
    created_by UUID NOT NULL REFERENCES users(id),
    is_published BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_tenant_course_due (tenant_id, course_id, due_date)
);

-- Submissions (Student Work)
CREATE TABLE submissions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    assignment_id UUID NOT NULL REFERENCES assignments(id),
    student_id UUID NOT NULL REFERENCES users(id),
    submission_text TEXT,
    submission_file_url VARCHAR(500),
    submitted_at TIMESTAMP,
    is_late BOOLEAN DEFAULT FALSE,
    grade INT,
    grade_comment TEXT,
    graded_at TIMESTAMP,
    graded_by UUID REFERENCES users(id),
    status ENUM('draft', 'submitted', 'graded', 'returned') DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(tenant_id, assignment_id, student_id),
    INDEX idx_tenant_assignment_student (tenant_id, assignment_id, student_id)
);

-- Attendance (Optional)
CREATE TABLE attendance (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    course_id UUID NOT NULL REFERENCES courses(id),
    student_id UUID NOT NULL REFERENCES users(id),
    date DATE NOT NULL,
    status ENUM('present', 'absent', 'late') DEFAULT 'absent',
    marked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(tenant_id, course_id, student_id, date),
    INDEX idx_tenant_course_date (tenant_id, course_id, date)
);

-- Audit Logs (For compliance)
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    user_id UUID REFERENCES users(id),
    action VARCHAR(100) NOT NULL,
    resource_type VARCHAR(100),
    resource_id VARCHAR(100),
    changes TEXT,
    ip_address VARCHAR(50),
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_tenant_timestamp (tenant_id, created_at)
);
```

### 3. Authentication & Authorization

**JWT Token Structure:**
```json
{
  "sub": "user-uuid",
  "tenant_id": "tenant-uuid",
  "email": "user@school.com",
  "role": "teacher",
  "exp": 1234567890,
  "iat": 1234567890
}
```

**Auth Endpoints:**
- `POST /auth/register` - Register new user
  - Input: email, password, full_name, role
  - Requires tenant_id in header or subdomain
  - Validation: email format, password strength
  
- `POST /auth/login` - Login user
  - Input: email, password
  - Output: access_token, refresh_token, user object
  - Tenant identified from email domain or header
  
- `POST /auth/refresh` - Refresh JWT token
  - Input: refresh_token
  - Output: new access_token
  
- `POST /auth/logout` - Logout (optional for JWT)
  - Blacklist token in Redis (if available)
  
- `GET /auth/me` - Get current user info
  - Requires valid JWT
  - Returns user object without password

- `POST /auth/verify-email` - Verify email
  - Input: verification_token
  - Sets email_verified = true

**Role-Based Access:**
- Admin: Full access to tenant data, user management, settings
- Teacher: Create courses, assignments; grade submissions; view enrolled students
- Student: View enrolled courses, submit assignments, view grades

### 4. API ENDPOINTS

**Base URL:** `/api/v1`

#### Authentication Routes
```
POST   /auth/register
POST   /auth/login
POST   /auth/refresh
POST   /auth/logout
GET    /auth/me
POST   /auth/verify-email
POST   /auth/forgot-password
POST   /auth/reset-password
```

#### User Management (Admin only)
```
GET    /users                          - List all users in tenant
GET    /users/{user_id}                - Get user details
PUT    /users/{user_id}                - Update user
DELETE /users/{user_id}                - Deactivate user
POST   /users/{user_id}/reset-password - Force password reset
GET    /users/statistics               - User statistics
```

#### Course Management
```
GET    /courses                        - List courses
POST   /courses                        - Create course (teachers/admin)
GET    /courses/{course_id}            - Get course details
PUT    /courses/{course_id}            - Update course
DELETE /courses/{course_id}            - Delete course

GET    /courses/{course_id}/enrollments - List enrolled students
POST   /courses/{course_id}/enrollments - Enroll student (admin/teacher)
DELETE /courses/{course_id}/enrollments/{student_id} - Drop student

GET    /courses/{course_id}/statistics - Course stats (grades, attendance)
```

#### Assignment Management
```
GET    /assignments                    - List assignments for courses
POST   /assignments                    - Create assignment (teachers)
GET    /assignments/{assignment_id}    - Get assignment details
PUT    /assignments/{assignment_id}    - Update assignment
DELETE /assignments/{assignment_id}    - Delete assignment
POST   /assignments/{assignment_id}/publish - Publish assignment

GET    /assignments/{assignment_id}/submissions - List submissions
```

#### Submission Management
```
GET    /submissions                    - List submissions for user
POST   /submissions                    - Create submission (students)
GET    /submissions/{submission_id}    - Get submission details
PUT    /submissions/{submission_id}    - Update submission (student)
DELETE /submissions/{submission_id}    - Delete submission (student)

PUT    /submissions/{submission_id}/grade - Grade submission (teacher)
POST   /submissions/{submission_id}/return - Return for revision

GET    /submissions/assignment/{assignment_id} - List submissions for assignment
```

#### Attendance Management
```
GET    /attendance                     - List attendance records
POST   /attendance                     - Mark attendance (teacher)
GET    /attendance/{student_id}        - Get student attendance
PUT    /attendance/{record_id}         - Update attendance record
```

#### Tenant Settings (Admin only)
```
GET    /tenant/settings                - Get tenant settings
PUT    /tenant/settings                - Update tenant settings
GET    /tenant/members                 - List tenant members
GET    /tenant/usage                   - Storage and resource usage
POST   /tenant/invite                  - Invite user to tenant
```

#### Health & Monitoring
```
GET    /health                         - Service health check
GET    /health/db                      - Database connectivity check
```

### 5. Implementation Requirements

#### Project Structure
```
backend/
├── main.py                   # FastAPI app initialization
├── requirements.txt          # Dependencies
├── Dockerfile               # Docker configuration
├── .env.example             # Example environment variables
│
├── app/
│   ├── __init__.py
│   ├── config.py            # Configuration management
│   ├── database.py          # Database connection/setup
│   ├── security.py          # JWT, password hashing
│   │
│   ├── middleware/
│   │   ├── auth.py          # JWT validation middleware
│   │   ├── tenant.py        # Tenant isolation middleware
│   │   └── logging.py       # Request/response logging
│   │
│   ├── models/
│   │   ├── tenant.py
│   │   ├── user.py
│   │   ├── course.py
│   │   ├── assignment.py
│   │   ├── submission.py
│   │   ├── attendance.py
│   │   └── audit_log.py
│   │
│   ├── schemas/              # Pydantic validation schemas
│   │   ├── user.py
│   │   ├── course.py
│   │   ├── assignment.py
│   │   ├── submission.py
│   │   └── common.py
│   │
│   ├── routes/
│   │   ├── auth.py          # Authentication routes
│   │   ├── users.py         # User management
│   │   ├── courses.py       # Course management
│   │   ├── assignments.py   # Assignment management
│   │   ├── submissions.py   # Submission handling
│   │   ├── attendance.py
│   │   ├── tenant.py        # Tenant settings
│   │   └── health.py        # Health checks
│   │
│   ├── services/             # Business logic
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── course_service.py
│   │   ├── submission_service.py
│   │   ├── s3_service.py     # AWS S3 integration
│   │   └── email_service.py  # Email notifications
│   │
│   ├── agents/               # Scheduled tasks/automation
│   │   ├── reminder_agent.py - Send assignment reminders
│   │   ├── grading_agent.py  - Auto-calculate grades
│   │   ├── notification_agent.py - Email notifications
│   │   └── cleanup_agent.py  - Archive old data
│   │
│   └── utils/
│       ├── exceptions.py     # Custom exceptions
│       ├── constants.py      # Constants, enums
│       └── helpers.py        # Utility functions
│
├── tests/                    # Unit tests
│   ├── test_auth.py
│   ├── test_courses.py
│   ├── test_submissions.py
│   └── conftest.py          # Pytest fixtures
│
├── migrations/               # Database migrations (Alembic)
│   └── versions/
│
└── docker-compose.yml        # Local development stack
```

#### Key Technologies & Libraries
```
FastAPI==0.104.1            # Web framework
SQLAlchemy==2.0.23          # ORM
psycopg2-binary==2.9.9      # PostgreSQL driver (or mysql connector)
python-jose==3.3.0          # JWT handling
passlib==1.7.4              # Password hashing
python-multipart==0.0.6     # Form data parsing
boto3==1.28.85              # AWS SDK
python-dotenv==1.0.0        # Environment variables
pydantic==2.5.0             # Data validation
pydantic-settings==2.1.0    # Settings management
APScheduler==3.10.4         # Scheduled tasks/agents
requests==2.31.0            # HTTP requests
python-dateutil==2.8.2      # Date utilities
```

#### Required Features Implementation

**1. Input Validation**
- Use Pydantic schemas for all inputs
- Validate email format, password strength
- Check UUID formats
- Sanitize text inputs

**2. Error Handling**
- Custom exception classes (AuthenticationError, TenantNotFound, etc.)
- Global error handler with proper HTTP status codes
- Structured error responses in JSON

**3. Logging**
- Structured JSON logging
- Log all API requests/responses
- Log authentication attempts
- Log all data modifications

**4. Security**
- Password hashing with bcrypt
- JWT token expiration (15 min access, 7 day refresh)
- Rate limiting on auth endpoints (5 attempts/minute)
- CORS configuration
- SQL injection prevention (ORM usage)
- XSS prevention (output encoding)

**5. AWS Integration**
- S3 file uploads for submissions
- Pre-signed URLs for secure downloads
- Environment variable configuration
- IAM role usage (no hardcoded keys in code)

**6. Agents/Scheduled Tasks**
- Assignment reminder (runs daily at 8 AM)
- Due date checker (mark late submissions)
- Grade notification (email when graded)
- Data cleanup (archive old assignments)

**7. Testing**
- Unit tests for services
- Integration tests for API endpoints
- Fixtures for test data
- Test database setup

### 6. Environment Variables (.env)
```
# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=student_lms
DB_USER=lms_user
DB_PASSWORD=secure_password
DATABASE_URL=postgresql://lms_user:secure_password@localhost:5432/student_lms

# JWT
JWT_SECRET_KEY=your-super-secret-key-change-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
REFRESH_TOKEN_EXPIRATION_DAYS=7

# AWS
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_S3_BUCKET_NAME=student-lms-uploads

# Email (for notifications)
EMAIL_SENDER=noreply@studentlms.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password

# Application
ENVIRONMENT=development
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,*.lms.local
CORS_ORIGINS=http://localhost:3000,http://localhost:5000

# External Services
SENTRY_DSN=  # Error tracking (optional)
```

### 7. Docker Setup

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000/api/v1/health')"

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15
    container_name: lms_postgres
    environment:
      POSTGRES_USER: lms_user
      POSTGRES_PASSWORD: secure_password
      POSTGRES_DB: student_lms
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - lms_network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U lms_user"]
      interval: 10s
      timeout: 5s
      retries: 5

  backend:
    build: .
    container_name: lms_backend
    ports:
      - "5000:5000"
    environment:
      DATABASE_URL: postgresql://lms_user:secure_password@postgres:5432/student_lms
      JWT_SECRET_KEY: dev-secret-key-change-in-production
      ENVIRONMENT: development
      AWS_S3_BUCKET_NAME: lms-local-bucket
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - lms_network
    volumes:
      - .:/app
    command: uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload

networks:
  lms_network:
    driver: bridge

volumes:
  postgres_data:
```

### 8. Deliverables Checklist

- [ ] Complete FastAPI application with all routes
- [ ] SQLAlchemy models for all entities
- [ ] Pydantic schemas for input validation
- [ ] Authentication with JWT
- [ ] Multi-tenant middleware and isolation
- [ ] S3 integration for file uploads
- [ ] Scheduled agents (APScheduler)
- [ ] Email notification system
- [ ] Error handling and logging
- [ ] Unit tests (minimum 70% coverage)
- [ ] Integration tests for API endpoints
- [ ] Database migrations (Alembic)
- [ ] Dockerfile and docker-compose.yml
- [ ] README with setup and API documentation
- [ ] Example .env file
- [ ] API documentation (FastAPI auto-docs at /docs)

### 9. Code Quality Standards

- Follow PEP 8 style guide
- Type hints on all functions
- Comprehensive docstrings
- No hardcoded values (use constants/env vars)
- No database credentials in code
- Proper error messages
- Consistent naming conventions

### 10. API Response Format

**Success Response:**
```json
{
  "success": true,
  "data": { ... },
  "message": "Operation successful"
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "VALIDATION_ERROR",
  "message": "Invalid email format",
  "details": [
    {
      "field": "email",
      "message": "Invalid email format"
    }
  ]
}
```

**Pagination Response:**
```json
{
  "success": true,
  "data": [ ... ],
  "pagination": {
    "total": 100,
    "page": 1,
    "page_size": 20,
    "total_pages": 5
  }
}
```

================================================================================

DELIVERABLE INSTRUCTIONS:

1. Generate COMPLETE, WORKING CODE
2. Code should run immediately with: docker-compose up --build
3. Include all files mentioned in project structure
4. Add comprehensive comments explaining logic
5. Include example requests/responses for each endpoint
6. Create sample data/seed script
7. Add migration files for database setup
8. Include comprehensive README with:
   - Setup instructions
   - How to run locally
   - API endpoint documentation
   - Testing instructions
   - Deployment guide to AWS EC2

START GENERATION NOW.
Make the code production-ready but educational (clear comments for learning).
```

---

## PART 3: ALTERNATIVE PROMPTS FOR DIFFERENT FRAMEWORKS

### If You Want Node.js (Express):

Replace the framework section with:
```
## BACKEND FRAMEWORK: Node.js with Express

Libraries:
- express==4.18.2
- sequelize==6.34.0 (ORM)
- passport==0.7.0 (authentication)
- jsonwebtoken==9.1.2
- bcryptjs==2.4.3
- dotenv==16.3.1
- aws-sdk==2.1485.0
- bull==4.11.5 (task queue for agents)
- joi==17.11.0 (validation)

[Rest of spec remains the same, adjust code examples to JavaScript/TypeScript]
```

### If You Want Go (Gin):

Replace the framework section with:
```
## BACKEND FRAMEWORK: Go 1.21 with Gin

Libraries:
- gin-gonic/gin (web framework)
- gorm.io/gorm (ORM)
- gorm.io/driver/postgres
- golang-jwt/jwt (JWT)
- aws/aws-sdk-go-v2 (AWS SDK)
- robfig/cron (scheduled tasks)

[Rest of spec remains the same, adjust code examples to Go]
```

---

## PART 4: TESTING STRATEGY

### Local Testing Before AWS Deployment

#### 1. Unit Tests
```bash
pytest app/tests/ -v --cov=app --cov-report=html
```

#### 2. Integration Tests
```bash
# Test API endpoints with docker-compose running
pytest app/tests/integration/ -v
```

#### 3. Manual Testing with Postman/cURL

**Create tenant:**
```bash
curl -X POST http://localhost:5000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@school1.com",
    "password": "SecurePass123!",
    "full_name": "School Admin",
    "role": "admin"
  }'
```

**Login:**
```bash
curl -X POST http://localhost:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@school1.com",
    "password": "SecurePass123!"
  }'
```

**Create course:**
```bash
curl -X POST http://localhost:5000/api/v1/courses \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Introduction to Python",
    "description": "Learn Python basics",
    "code": "PY101"
  }'
```

---

## PART 5: MIGRATION TO AWS

### Checklist:
- [ ] Local testing complete
- [ ] All environment variables configured
- [ ] AWS account created and verified
- [ ] EC2 instance launched (t2.micro)
- [ ] RDS instance created (db.t2.micro)
- [ ] Security groups configured
- [ ] SSH key pair saved securely
- [ ] Docker hub account created
- [ ] Project pushed to GitHub (private repo)
- [ ] AWS credentials created for application
- [ ] S3 bucket created for file uploads
- [ ] Docker image built and tested
- [ ] Deployed to EC2 and verified running
- [ ] CloudWatch monitoring configured
- [ ] Backup strategy implemented

