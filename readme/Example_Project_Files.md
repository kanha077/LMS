# AWS LMS Project - Example Files & Structure

## Project Folder Structure Example

```
StudentLMS/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                  (FastAPI app)
│   │   ├── config.py                (Configuration)
│   │   ├── database.py              (Database setup)
│   │   ├── security.py              (JWT, hashing)
│   │   │
│   │   ├── middleware/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py              (JWT validation)
│   │   │   └── tenant.py            (Tenant isolation)
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── tenant.py
│   │   │   ├── user.py
│   │   │   ├── course.py
│   │   │   ├── assignment.py
│   │   │   └── submission.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── user.py              (Pydantic models)
│   │   │   ├── course.py
│   │   │   └── common.py
│   │   │
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── courses.py
│   │   │   ├── assignments.py
│   │   │   ├── submissions.py
│   │   │   └── health.py
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py
│   │   │   ├── course_service.py
│   │   │   ├── submission_service.py
│   │   │   └── email_service.py
│   │   │
│   │   ├── agents/
│   │   │   ├── __init__.py
│   │   │   ├── reminder_agent.py    (Scheduled tasks)
│   │   │   └── notification_agent.py
│   │   │
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── exceptions.py
│   │       └── constants.py
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py              (Pytest fixtures)
│   │   ├── test_auth.py
│   │   └── test_courses.py
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .dockerignore
│   └── .env.example
│
├── database/
│   ├── init.sql                     (Initial schema)
│   └── migrations/
│       ├── 001_initial_schema.sql
│       └── 002_add_audit_logs.sql
│
├── docker-compose.yml
├── .gitignore
├── README.md
└── docs/
    ├── API.md
    ├── DEPLOYMENT.md
    └── TROUBLESHOOTING.md
```

---

## Example: requirements.txt

```
FastAPI==0.104.1
uvicorn[standard]==0.24.0
SQLAlchemy==2.0.23
psycopg2-binary==2.9.9
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
boto3==1.28.85
python-dotenv==1.0.0
pydantic==2.5.0
pydantic-settings==2.1.0
APScheduler==3.10.4
python-dateutil==2.8.2
pytest==7.4.3
pytest-asyncio==0.21.1
httpx==0.25.2
```

---

## Example: Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import httpx; httpx.get('http://localhost:5000/api/v1/health')" || exit 1

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
```

---

## Example: .env.example

```
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=student_lms
DB_USER=lms_user
DB_PASSWORD=change_me_in_production
DATABASE_URL=postgresql://lms_user:change_me@localhost:5432/student_lms

# JWT Configuration
JWT_SECRET_KEY=your-super-secret-key-change-in-production-min-32-chars
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
REFRESH_TOKEN_EXPIRATION_DAYS=7

# AWS Configuration
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_S3_BUCKET_NAME=student-lms-uploads

# Application Configuration
ENVIRONMENT=development
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ORIGINS=http://localhost:3000,http://localhost:5000

# Email Configuration (for notifications)
EMAIL_SENDER=noreply@studentlms.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password
```

---

## Example: app/main.py

```python
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.config import settings
from app.database import engine, Base
from app.middleware.auth import JWTAuthMiddleware
from app.middleware.tenant import TenantMiddleware
from app.routes import auth, courses, assignments, submissions, health
from app.utils.exceptions import ApplicationException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize database tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting up application...")
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown
    logger.info("Shutting down application...")

# Create FastAPI application
app = FastAPI(
    title="Student LMS API",
    description="Multi-tenant Learning Management System",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add custom middleware
app.add_middleware(TenantMiddleware)
app.add_middleware(JWTAuthMiddleware)

# Exception handler
@app.exception_handler(ApplicationException)
async def application_exception_handler(request: Request, exc: ApplicationException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.error_code,
            "message": exc.message,
            "details": exc.details
        }
    )

# Include routes
app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(courses.router, prefix="/api/v1", tags=["courses"])
app.include_router(assignments.router, prefix="/api/v1", tags=["assignments"])
app.include_router(submissions.router, prefix="/api/v1", tags=["submissions"])

# Health check endpoint
@app.get("/")
def root():
    return {
        "message": "Student LMS API",
        "version": "1.0.0",
        "docs": "/api/v1/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5000,
        reload=settings.DEBUG
    )
```

---

## Example: app/config.py

```python
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Database
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "student_lms"
    DB_USER: str = "lms_user"
    DB_PASSWORD: str = "password"
    
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    # JWT
    JWT_SECRET_KEY: str = "change-me-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24
    REFRESH_TOKEN_EXPIRATION_DAYS: int = 7
    
    # AWS
    AWS_REGION: str = "us-east-1"
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_S3_BUCKET_NAME: str = "student-lms-uploads"
    
    # Application
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5000"]
    
    # Email
    EMAIL_SENDER: str = "noreply@studentlms.com"
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    
    class Config:
        env_file = ".env"

# Create settings instance
settings = Settings()
```

---

## Example: app/models/user.py

```python
from sqlalchemy import Column, String, Boolean, DateTime, Enum, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
import enum

from app.database import Base

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    email = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255))
    role = Column(Enum(UserRole), default=UserRole.STUDENT)
    is_active = Column(Boolean, default=True)
    email_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    __table_args__ = (
        Index('idx_tenant_email', 'tenant_id', 'email'),
    )
    
    def __repr__(self):
        return f"<User {self.email}>"
```

---

## Example: app/schemas/user.py

```python
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: str
    role: str = "student"

class UserResponse(BaseModel):
    id: UUID
    email: str
    full_name: str
    role: str
    is_active: bool
    email_verified: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
```

---

## Example: app/routes/auth.py

```python
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from datetime import timedelta

from app.database import get_db
from app.schemas.user import UserCreate, UserResponse, LoginRequest
from app.services.auth_service import AuthService
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])
auth_service = AuthService()

@router.post("/register", response_model=dict)
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user
    """
    try:
        user = auth_service.register_user(db, user_data)
        return {
            "success": True,
            "message": "User registered successfully",
            "data": UserResponse.from_orm(user)
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=dict)
async def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    """
    Login user and return JWT token
    """
    user = auth_service.authenticate_user(db, credentials.email, credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = auth_service.create_access_token(user)
    refresh_token = auth_service.create_refresh_token(user)
    
    return {
        "success": True,
        "data": {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": UserResponse.from_orm(user)
        }
    }

@router.get("/me", response_model=dict)
async def get_current_user(current_user: User = Depends(auth_service.get_current_user)):
    """
    Get current authenticated user
    """
    return {
        "success": True,
        "data": UserResponse.from_orm(current_user)
    }
```

---

## Example: docker-compose.yml

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    container_name: lms_postgres
    environment:
      POSTGRES_USER: lms_user
      POSTGRES_PASSWORD: secure_password_change_me
      POSTGRES_DB: student_lms
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./database/init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - lms_network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U lms_user"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    container_name: lms_redis
    ports:
      - "6379:6379"
    networks:
      - lms_network
    restart: unless-stopped

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: lms_backend
    ports:
      - "5000:5000"
    environment:
      DATABASE_URL: postgresql://lms_user:secure_password_change_me@postgres:5432/student_lms
      JWT_SECRET_KEY: dev-secret-key-min-32-characters-change-in-production
      ENVIRONMENT: development
      DEBUG: "True"
      AWS_REGION: us-east-1
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - lms_network
    volumes:
      - ./backend:/app
    command: uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
    restart: unless-stopped

networks:
  lms_network:
    driver: bridge

volumes:
  postgres_data:
```

---

## Example: database/init.sql

```sql
-- Create UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Tenants table
CREATE TABLE tenants (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    subdomain VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255),
    subscription_plan VARCHAR(50) DEFAULT 'free',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    role VARCHAR(50) DEFAULT 'student',
    is_active BOOLEAN DEFAULT TRUE,
    email_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(tenant_id, email)
);
CREATE INDEX idx_tenant_email ON users(tenant_id, email);

-- Courses table
CREATE TABLE courses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    code VARCHAR(50) NOT NULL,
    teacher_id UUID NOT NULL REFERENCES users(id),
    semester VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(tenant_id, code)
);
CREATE INDEX idx_tenant_teacher ON courses(tenant_id, teacher_id);

-- Assignments table
CREATE TABLE assignments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    instructions TEXT,
    due_date TIMESTAMP NOT NULL,
    total_points INTEGER DEFAULT 100,
    created_by UUID NOT NULL REFERENCES users(id),
    is_published BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_tenant_course_due ON assignments(tenant_id, course_id, due_date);

-- Submissions table
CREATE TABLE submissions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    assignment_id UUID NOT NULL REFERENCES assignments(id) ON DELETE CASCADE,
    student_id UUID NOT NULL REFERENCES users(id),
    submission_text TEXT,
    submission_file_url VARCHAR(500),
    submitted_at TIMESTAMP,
    is_late BOOLEAN DEFAULT FALSE,
    grade INTEGER,
    grade_comment TEXT,
    graded_at TIMESTAMP,
    graded_by UUID REFERENCES users(id),
    status VARCHAR(50) DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(tenant_id, assignment_id, student_id)
);
CREATE INDEX idx_tenant_assignment_student ON submissions(tenant_id, assignment_id, student_id);
```

---

## Example: README.md Template

```markdown
# Student LMS - Learning Management System

A multi-tenant, production-ready Learning Management System built with FastAPI, PostgreSQL, and AWS.

## Features

- 🏫 **Multi-Tenant Architecture** - Multiple organizations on single instance
- 👤 **Role-Based Access Control** - Admin, Teacher, Student roles
- 📚 **Course Management** - Create and manage courses
- ✏️ **Assignment & Submission System** - Post assignments, students submit work
- 📊 **Grading System** - Teachers grade submissions
- 🔐 **Secure Authentication** - JWT-based authentication
- 📁 **File Storage** - AWS S3 integration for file uploads
- 🤖 **Automation Agents** - Scheduled tasks for reminders and notifications
- 📝 **Audit Logging** - Track all user actions

## Prerequisites

- Docker Desktop (Windows/Mac) or Docker (Linux)
- Git
- AWS Account (free tier)

## Local Development Setup

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/StudentLMS.git
cd StudentLMS
```

### 2. Create Environment File
```bash
cp backend/.env.example backend/.env
# Edit .env with your values
```

### 3. Start with Docker Compose
```bash
docker-compose up -d --build
```

### 4. Access Application
- API: http://localhost:5000
- API Docs: http://localhost:5000/api/v1/docs
- Database: localhost:5432

## API Documentation

### Authentication

#### Register User
```bash
curl -X POST http://localhost:5000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "SecurePassword123!",
    "full_name": "John Doe",
    "role": "student"
  }'
```

#### Login
```bash
curl -X POST http://localhost:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "SecurePassword123!"
  }'
```

#### Get Current User
```bash
curl -X GET http://localhost:5000/api/v1/auth/me \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## Testing

### Run All Tests
```bash
docker-compose exec backend pytest -v
```

### Run Specific Test
```bash
docker-compose exec backend pytest app/tests/test_auth.py -v
```

### Run with Coverage
```bash
docker-compose exec backend pytest --cov=app --cov-report=html
```

## Deployment to AWS

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed AWS deployment steps.

### Quick Deploy
```bash
# 1. Create EC2 instance (t2.micro)
# 2. Create RDS database (db.t2.micro)
# 3. SSH to EC2 and run:
git clone https://github.com/YOUR_USERNAME/StudentLMS.git
cd StudentLMS
docker-compose up -d --build
```

## Project Structure

- `backend/` - FastAPI application
  - `app/` - Main application code
    - `routes/` - API endpoints
    - `models/` - SQLAlchemy models
    - `schemas/` - Pydantic schemas
    - `services/` - Business logic
    - `agents/` - Scheduled tasks
- `database/` - Database migrations and init scripts
- `tests/` - Test files
- `docker-compose.yml` - Local development stack

## Environment Variables

See `backend/.env.example` for all required variables.

Key variables:
- `DATABASE_URL` - PostgreSQL connection string
- `JWT_SECRET_KEY` - Secret key for JWT tokens
- `AWS_ACCESS_KEY_ID` - AWS access key
- `AWS_SECRET_ACCESS_KEY` - AWS secret key
- `AWS_S3_BUCKET_NAME` - S3 bucket for file uploads

## Troubleshooting

### Database Connection Error
```bash
# Check database is running
docker-compose ps

# View database logs
docker-compose logs postgres
```

### API Not Responding
```bash
# View backend logs
docker-compose logs -f backend

# Check health
curl http://localhost:5000/api/v1/health
```

### Port Already in Use
```bash
# Change port in docker-compose.yml
# Change "5000:5000" to "5001:5000"
docker-compose down
docker-compose up -d --build
```

## Contributing

1. Create feature branch
2. Make changes
3. Write tests
4. Submit pull request

## License

MIT

## Support

For issues and questions, please create an issue on GitHub.
```

---

## How to Use These Files

1. **Copy this structure** to your project folder
2. **Update docker-compose.yml** with your database password
3. **Update .env** with actual AWS credentials
4. **Run locally first**:
   ```powershell
   docker-compose up -d --build
   ```
5. **Test with curl or Postman**
6. **Then deploy to AWS EC2**

