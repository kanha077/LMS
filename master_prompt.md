# Backend + Vue Frontend Prompts for Student LMS

## IMPORTANT: TWO-STEP PROCESS

You'll use these prompts in this order:

1. **STEP 1 (Now):** Use Backend Prompt with Claude/Anthropic
   - Get working backend API
   - Test it locally with docker-compose
   - Verify all endpoints work

2. **STEP 2 (After backend works):** Use Frontend Prompt with Claude/Anthropic
   - Get Vue.js frontend
   - Test it locally
   - Connect to backend
   - Deploy both together

---

# PROMPT 1: BACKEND API (Use This First)

Copy and paste this entire prompt to Claude:

```
SYSTEM CONTEXT:
You are an expert backend architect creating a production-grade Multi-Tenant 
Student Learning Management System (LMS). This is an educational project that 
will be deployed on AWS with a Vue.js frontend. Code must be:
- Clean, well-documented, and follows best practices
- Ready to run immediately with docker-compose
- Secure (JWT auth, input validation, SQL injection prevention)
- Scalable (multi-tenant architecture)
- AWS-ready (S3 integration, environment variables)
- CORS-enabled for Vue frontend
- Complete with CRUD operations

================================================================================

PROJECT SPECIFICATION:

## BACKEND FRAMEWORK: Python 3.11+ with FastAPI

## SCOPE:
Create a complete, working REST API backend with database schema, authentication,
and core business logic. Frontend will be built separately in Vue.js.

This backend must be:
1. Fully functional (can test endpoints with /docs)
2. CORS-enabled for localhost:3000 (Vue frontend)
3. Return JSON responses in consistent format
4. Implement all business logic
5. Include file upload to S3
6. Include scheduled agents

## ARCHITECTURE REQUIREMENTS:

### 1. Multi-Tenancy Design
- Every data table must have 'tenant_id' column
- Users can only access data from their tenant
- Tenant identified by subdomain or request header
- Tenant validation in middleware for every request
- Tenant isolation at database level

### 2. Database Schema (PostgreSQL)

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
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    avatar_url VARCHAR(500),
    role ENUM('admin', 'teacher', 'student') DEFAULT 'student',
    is_active BOOLEAN DEFAULT TRUE,
    email_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(tenant_id, email)
);
CREATE INDEX idx_tenant_email ON users(tenant_id, email);

-- Courses
CREATE TABLE courses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    code VARCHAR(50) NOT NULL,
    teacher_id UUID NOT NULL REFERENCES users(id),
    semester VARCHAR(50),
    max_students INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(tenant_id, code)
);
CREATE INDEX idx_tenant_teacher ON courses(tenant_id, teacher_id);

-- Course Enrollments
CREATE TABLE course_enrollments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    student_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    grade VARCHAR(2),
    status ENUM('active', 'dropped', 'completed') DEFAULT 'active',
    UNIQUE(tenant_id, course_id, student_id)
);
CREATE INDEX idx_tenant_course_student ON course_enrollments(tenant_id, course_id, student_id);

-- Assignments
CREATE TABLE assignments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    instructions TEXT,
    due_date TIMESTAMP NOT NULL,
    total_points INT DEFAULT 100,
    created_by UUID NOT NULL REFERENCES users(id),
    is_published BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_tenant_course_due ON assignments(tenant_id, course_id, due_date);

-- Submissions
CREATE TABLE submissions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    assignment_id UUID NOT NULL REFERENCES assignments(id) ON DELETE CASCADE,
    student_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
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
    UNIQUE(tenant_id, assignment_id, student_id)
);
CREATE INDEX idx_tenant_assignment_student ON submissions(tenant_id, assignment_id, student_id);

-- Attendance
CREATE TABLE attendance (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    student_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    status ENUM('present', 'absent', 'late') DEFAULT 'absent',
    marked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(tenant_id, course_id, student_id, date)
);

-- Audit Logs
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(id),
    action VARCHAR(100) NOT NULL,
    resource_type VARCHAR(100),
    resource_id VARCHAR(100),
    changes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
  "exp": 1234567890
}
```

**Auth Endpoints:**
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login user (returns access & refresh tokens)
- `POST /api/v1/auth/refresh` - Refresh JWT token
- `GET /api/v1/auth/me` - Get current user
- `POST /api/v1/auth/logout` - Logout

### 4. API ENDPOINTS

**Base URL:** `/api/v1`

**CORS Configuration:**
```
Allow:
- localhost:3000 (Vue frontend)
- localhost:5000 (for testing)
- http://localhost:* (development)

Allow Methods: GET, POST, PUT, DELETE, OPTIONS
Allow Headers: Authorization, Content-Type
```

#### Auth Endpoints
```
POST   /auth/register              - Register user
POST   /auth/login                 - Login user
POST   /auth/refresh               - Refresh token
GET    /auth/me                    - Current user
POST   /auth/logout                - Logout
```

#### User Management
```
GET    /users                      - List users (admin only)
GET    /users/{user_id}            - Get user details
PUT    /users/{user_id}            - Update user
DELETE /users/{user_id}            - Deactivate user
GET    /users/search               - Search users by name/email
```

#### Course Management
```
GET    /courses                    - List courses
POST   /courses                    - Create course (teacher/admin)
GET    /courses/{course_id}        - Get course details
PUT    /courses/{course_id}        - Update course
DELETE /courses/{course_id}        - Delete course
GET    /courses/{course_id}/students - List enrolled students
POST   /courses/{course_id}/enroll/{student_id} - Enroll student
DELETE /courses/{course_id}/enroll/{student_id} - Drop student
GET    /courses/{course_id}/stats  - Course statistics
```

#### Assignment Management
```
GET    /assignments                - List assignments for user's courses
POST   /assignments                - Create assignment (teacher)
GET    /assignments/{id}           - Get assignment details
PUT    /assignments/{id}           - Update assignment
DELETE /assignments/{id}           - Delete assignment
POST   /assignments/{id}/publish   - Publish assignment
GET    /assignments/{id}/submissions - List submissions for assignment
```

#### Submission Management
```
GET    /submissions                - List submissions for user
POST   /submissions                - Create submission (student)
GET    /submissions/{id}           - Get submission details
PUT    /submissions/{id}           - Update submission (student)
DELETE /submissions/{id}           - Delete submission (student)
POST   /submissions/{id}/submit    - Mark as submitted
PUT    /submissions/{id}/grade     - Grade submission (teacher)
POST   /submissions/{id}/return    - Return for revision (teacher)
GET    /assignments/{id}/submissions - Get all submissions for assignment
```

#### Attendance
```
GET    /attendance                 - List attendance records
POST   /attendance                 - Mark attendance (teacher)
GET    /attendance/{student_id}    - Get student attendance
PUT    /attendance/{id}            - Update attendance record
```

#### Health & Info
```
GET    /health                     - Service health
GET    /health/db                  - Database health
```

### 5. Response Format

**Success Response:**
```json
{
  "success": true,
  "data": {},
  "message": "Operation successful"
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "ERROR_CODE",
  "message": "Human readable message",
  "details": []
}
```

**Paginated Response:**
```json
{
  "success": true,
  "data": [],
  "pagination": {
    "total": 100,
    "page": 1,
    "page_size": 20,
    "total_pages": 5
  }
}
```

### 6. Implementation Requirements

#### Project Structure
```
backend/
├── main.py
├── requirements.txt
├── Dockerfile
├── .env.example
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── security.py
│   ├── middleware/
│   │   ├── auth.py
│   │   ├── tenant.py
│   │   └── cors.py
│   ├── models/
│   │   ├── tenant.py
│   │   ├── user.py
│   │   ├── course.py
│   │   ├── assignment.py
│   │   ├── submission.py
│   │   └── attendance.py
│   ├── schemas/
│   │   ├── user.py
│   │   ├── course.py
│   │   ├── assignment.py
│   │   ├── submission.py
│   │   └── common.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── courses.py
│   │   ├── assignments.py
│   │   ├── submissions.py
│   │   ├── attendance.py
│   │   └── health.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── course_service.py
│   │   ├── submission_service.py
│   │   ├── s3_service.py
│   │   └── email_service.py
│   ├── agents/
│   │   ├── reminder_agent.py
│   │   ├── notification_agent.py
│   │   └── grading_agent.py
│   └── utils/
│       ├── exceptions.py
│       ├── constants.py
│       └── helpers.py
├── database/
│   └── init.sql
└── tests/
```

#### Libraries
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
APScheduler==3.10.4
pytest==7.4.3
httpx==0.25.2
```

### 7. Key Features

**CORS Configuration:**
- Enable CORS for http://localhost:3000 (Vue frontend)
- Enable CORS for http://localhost:5000 (testing)
- Allow credentials
- Allow all methods

**JWT Authentication:**
- 15 minute access token
- 7 day refresh token
- Blacklist on logout

**Multi-Tenant Isolation:**
- Middleware extracts tenant from header or subdomain
- Every query filtered by tenant_id
- Users can only access own tenant data

**File Upload:**
- S3 integration for submission files
- Pre-signed URLs for downloads
- File size limits

**Scheduled Agents:**
- Assignment reminders (daily 8 AM)
- Grade notifications (immediately on grade)
- Overdue submission marking

**Error Handling:**
- Custom exception classes
- Global error handler
- Proper HTTP status codes
- Structured error responses

**Validation:**
- Input validation with Pydantic
- Email format validation
- Password strength requirements
- File upload validation

### 8. Environment Variables

```
# Database
DATABASE_URL=postgresql://lms_user:password@localhost:5432/student_lms

# JWT
JWT_SECRET_KEY=your-secret-key-min-32-chars
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
REFRESH_TOKEN_EXPIRATION_DAYS=7

# AWS
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_S3_BUCKET_NAME=student-lms-uploads

# Application
ENVIRONMENT=development
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ORIGINS=http://localhost:3000,http://localhost:5000

# Email
EMAIL_SENDER=noreply@studentlms.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email
SMTP_PASSWORD=your_password
```

### 9. Docker Configuration

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import httpx; httpx.get('http://localhost:5000/api/v1/health')" || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    container_name: lms_postgres
    environment:
      POSTGRES_USER: lms_user
      POSTGRES_PASSWORD: secure_password
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

  backend:
    build: .
    container_name: lms_backend
    ports:
      - "5000:5000"
    environment:
      DATABASE_URL: postgresql://lms_user:secure_password@postgres:5432/student_lms
      JWT_SECRET_KEY: dev-secret-key-min-32-chars-change-in-production
      CORS_ORIGINS: http://localhost:3000,http://localhost:5000
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

### 10. Deliverables

- [ ] Complete FastAPI application with all endpoints
- [ ] SQLAlchemy models for all entities
- [ ] Pydantic schemas for validation
- [ ] JWT authentication system
- [ ] Multi-tenant middleware and isolation
- [ ] S3 file upload integration
- [ ] Scheduled agents/automation
- [ ] Email notification system
- [ ] CORS configuration for Vue frontend
- [ ] Error handling and logging
- [ ] Database initialization script
- [ ] Dockerfile and docker-compose.yml
- [ ] README with setup instructions
- [ ] Example .env file
- [ ] API documentation (FastAPI /docs)
- [ ] Unit tests
- [ ] Seed data script

================================================================================

DELIVERABLE INSTRUCTIONS:

1. Generate COMPLETE, WORKING CODE
2. Code should run with: docker-compose up --build
3. Include all files from project structure
4. Add comprehensive comments
5. Create example requests for each endpoint
6. Add database seed script
7. Include README with setup and API docs
8. Make it CORS-enabled for Vue frontend at localhost:3000
9. Code should be production-quality but educational

START GENERATION NOW.
```

---

# PROMPT 2: FRONTEND (Use This AFTER Backend Works)

Save this for later. Once your backend is working locally, use this prompt:

```
SYSTEM CONTEXT:
You are an expert frontend developer creating a clean, modern Vue.js 3 interface 
for a multi-tenant Student Learning Management System. This is an educational 
project that connects to a FastAPI backend API at http://localhost:5000.

The interface should be:
- Clean and intuitive (student/teacher-friendly)
- Responsive (works on desktop and tablet)
- Simple HTML/Vue (no complex build tools)
- Uses Tailwind CSS for styling
- Connects to backend API at localhost:5000
- Supports three roles: Admin, Teacher, Student

================================================================================

PROJECT SPECIFICATION:

## FRONTEND FRAMEWORK: Vue.js 3 + HTML/CSS (Tailwind)

## SCOPE:
Create a complete, working web interface with all pages needed for:
1. Authentication (login/register)
2. Student dashboard
3. Teacher dashboard
4. Admin dashboard
5. Course management
6. Assignment viewing and submission
7. Grading system

## TECHNOLOGY STACK:

- Vue.js 3 (composition API)
- Tailwind CSS (styling)
- Axios (API calls)
- Vue Router (navigation)
- No build tools (direct CDN imports, simpler for learning)

Alternative: Can use Vite build tool if preferred

## PROJECT STRUCTURE:

```
frontend/
├── index.html              (Entry point)
├── package.json            (Scripts, minimal)
├── public/
│   ├── css/
│   │   └── tailwind.css
│   ├── js/
│   │   ├── main.js         (Vue app initialization)
│   │   ├── router.js       (Route definitions)
│   │   ├── api.js          (API client)
│   │   └── store.js        (Auth state management)
│   └── images/
│       └── logo.png
├── src/
│   ├── components/
│   │   ├── Navbar.vue
│   │   ├── Sidebar.vue
│   │   ├── LoadingSpinner.vue
│   │   ├── ConfirmModal.vue
│   │   ├── ErrorAlert.vue
│   │   └── SuccessAlert.vue
│   ├── pages/
│   │   ├── auth/
│   │   │   ├── Login.vue
│   │   │   ├── Register.vue
│   │   │   └── ForgotPassword.vue
│   │   ├── dashboard/
│   │   │   ├── StudentDashboard.vue
│   │   │   ├── TeacherDashboard.vue
│   │   │   └── AdminDashboard.vue
│   │   ├── courses/
│   │   │   ├── CourseList.vue
│   │   │   ├── CourseDetail.vue
│   │   │   ├── CreateCourse.vue
│   │   │   ├── EnrollCourse.vue
│   │   │   └── ManageStudents.vue
│   │   ├── assignments/
│   │   │   ├── AssignmentList.vue
│   │   │   ├── AssignmentDetail.vue
│   │   │   ├── CreateAssignment.vue
│   │   │   ├── SubmitAssignment.vue
│   │   │   └── GradeSubmission.vue
│   │   ├── submissions/
│   │   │   ├── SubmissionList.vue
│   │   │   ├── SubmissionDetail.vue
│   │   │   └── ViewGrades.vue
│   │   ├── admin/
│   │   │   ├── UserManagement.vue
│   │   │   ├── TenantSettings.vue
│   │   │   └── Analytics.vue
│   │   └── NotFound.vue
│   ├── assets/
│   └── styles/
│       └── app.css         (Global styles)
├── Dockerfile             (Optional, for containerization)
└── .env.example
```

## PAGES TO CREATE:

### 1. Authentication Pages
- **Login Page**
  - Email input
  - Password input
  - "Remember me" checkbox
  - Login button
  - Link to register
  - Error messages display

- **Register Page**
  - Email input
  - Password input (with strength indicator)
  - Confirm password
  - Full name
  - Role selector (if admin allows)
  - Terms checkbox
  - Register button
  - Link to login

### 2. Navigation
- **Navbar** (top)
  - Logo
  - Current user name
  - Notification bell (if notifications)
  - Logout button
  - Settings dropdown

- **Sidebar** (left)
  - Different menu for each role
  - Navigation links
  - Active page indicator
  - Collapsible on mobile

### 3. Dashboard Pages (Different for each role)

**Student Dashboard:**
- Welcome message with student name
- List of enrolled courses (cards)
- Upcoming assignments (with due dates)
- Recent grades
- Quick stats (GPA, assignments submitted, etc.)

**Teacher Dashboard:**
- List of courses taught
- Recent submissions to grade
- Quick stats (students, assignments posted)
- Notifications/messages

**Admin Dashboard:**
- Tenant information
- User count statistics
- Storage usage (S3)
- Recent activity log
- Quick links to management pages

### 4. Course Management

**Course List Page:**
- List all courses (pagination)
- Search and filter
- "Create Course" button (teachers/admin)
- Join/Leave course buttons
- Course cards showing:
  - Course name
  - Teacher name
  - Student count
  - Last updated

**Course Detail Page:**
- Course name and description
- List of assignments
- List of enrolled students (if teacher)
- Enroll button (if student)
- Course materials section

**Create Course Page:**
- Form to create new course
- Course name
- Description
- Code
- Semester
- Submit button

**Manage Students Page:**
- List enrolled students
- Add/Remove students
- Search students

### 5. Assignment Management

**Assignment List Page:**
- List assignments for selected course
- Filter by status (published, draft)
- "Create Assignment" button (teacher)
- Assignment cards showing:
  - Title
  - Due date
  - Points
  - Status

**Assignment Detail Page:**
- Full assignment description
- Due date and time
- Instructions
- Student submission status (if teacher)
- Submit button (if student)

**Create Assignment Page:**
- Form for teachers
- Title
- Description
- Instructions
- Due date/time picker
- Points/rubric
- Publish button

**Submit Assignment Page:**
- Show assignment details
- Text input area for submission (if text)
- File upload input (if file upload)
- Submit button
- Show previous submissions (if exists)

### 6. Grading

**Grade Submission Page:**
- Show student's submission
- Display file (if uploaded) or text
- Input field for grade/points
- Comment area
- "Save Grade" button

**View Grades Page (Student):**
- List of submissions with grades
- Show grade, points, teacher comment
- Download submission files

### 7. Admin Pages

**User Management:**
- List all users in tenant
- Search users
- Edit user role/status
- Delete user

**Tenant Settings:**
- Organization name
- Email
- Subscription plan
- Danger zone (delete tenant)

**Analytics Dashboard:**
- Charts showing:
  - Users over time
  - Submissions over time
  - Grades distribution
  - Most active courses

## KEY FEATURES:

### Authentication Flow
1. User opens app
2. Check localStorage for token
3. If token exists, verify with backend
4. If valid, redirect to dashboard
5. If invalid, redirect to login

### API Integration
- All API calls to: http://localhost:5000/api/v1
- Send JWT token in Authorization header
- Handle errors and display messages
- Loading states for async operations

### State Management (Simple)
```javascript
// Store in localStorage:
- access_token
- refresh_token
- user (id, email, role, tenant_id)
- tenant_id

// Or use Vue composable for reactive state
```

### Styling with Tailwind
- Responsive breakpoints
- Color scheme (professional)
- Button styles (primary, secondary)
- Form styles
- Card layouts
- Modal/dialog styles

### Error Handling
- API error messages displayed to user
- Form validation errors
- Network error handling
- 401 (unauthorized) redirects to login
- 403 (forbidden) shows permission error

### Loading States
- Show spinner during API calls
- Disable buttons while loading
- Show skeleton loaders (optional)

## PAGES TO BUILD (18 Total)

1. Login.vue
2. Register.vue
3. StudentDashboard.vue
4. TeacherDashboard.vue
5. AdminDashboard.vue
6. CourseList.vue
7. CourseDetail.vue
8. CreateCourse.vue
9. ManageStudents.vue
10. AssignmentList.vue
11. AssignmentDetail.vue
12. CreateAssignment.vue
13. SubmitAssignment.vue
14. GradeSubmission.vue
15. SubmissionList.vue
16. ViewGrades.vue
17. UserManagement.vue
18. TenantSettings.vue

Plus Components:
- Navbar.vue
- Sidebar.vue
- LoadingSpinner.vue
- ConfirmModal.vue
- ErrorAlert.vue
- SuccessAlert.vue

## API ENDPOINTS TO CALL:

```
POST   /auth/login
POST   /auth/register
GET    /auth/me
POST   /auth/logout

GET    /courses
POST   /courses
GET    /courses/{id}
PUT    /courses/{id}
DELETE /courses/{id}
POST   /courses/{id}/enroll/{student_id}
DELETE /courses/{id}/enroll/{student_id}
GET    /courses/{id}/students
GET    /courses/{id}/stats

GET    /assignments
POST   /assignments
GET    /assignments/{id}
PUT    /assignments/{id}
POST   /assignments/{id}/publish

GET    /submissions
POST   /submissions
GET    /submissions/{id}
PUT    /submissions/{id}
POST   /submissions/{id}/submit
PUT    /submissions/{id}/grade
GET    /assignments/{id}/submissions

GET    /users
PUT    /users/{id}
DELETE /users/{id}
```

## TECHNICAL REQUIREMENTS:

### Build Tools
Option 1 (Recommended for learning): No build tools
- Use CDN imports for libraries
- Single HTML file or simple folder structure
- Direct script includes

Option 2: Vite (if you want modern build)
- npm init vue@latest
- Vite dev server
- Build optimization

### Libraries to Use
```html
<!-- Vue 3 -->
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

<!-- Vue Router -->
<script src="https://unpkg.com/vue-router@4/dist/vue-router.global.js"></script>

<!-- Axios (API calls) -->
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

<!-- Tailwind CSS -->
<link href="https://cdn.tailwindcss.com" rel="stylesheet">

<!-- Icons (optional) -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
```

### API Client Setup
```javascript
// api.js
const API_BASE_URL = 'http://localhost:5000/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Add token to requests
apiClient.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle 401 errors
apiClient.interceptors.response.use(
  response => response,
  error => {
    if (error.response.status === 401) {
      // Redirect to login
      router.push('/login');
      localStorage.clear();
    }
    return Promise.reject(error);
  }
);

export default apiClient;
```

### Authentication Store
```javascript
// store.js
const store = {
  user: null,
  tenant_id: null,
  access_token: null,
  
  async login(email, password) {
    // Call API
    // Store tokens and user
  },
  
  async logout() {
    // Clear localStorage
    // Redirect to login
  },
  
  isAuthenticated() {
    return this.access_token !== null;
  },
  
  isRole(role) {
    return this.user?.role === role;
  }
};
```

## STYLING GUIDELINES:

- **Colors**: Professional blue/gray theme
- **Typography**: Clear hierarchy
- **Spacing**: Consistent padding/margins
- **Buttons**: 
  - Primary (blue): Main actions
  - Secondary (gray): Alternative actions
  - Danger (red): Delete/logout
- **Forms**: Proper labels, error messages
- **Responsive**: Mobile-first design

## DELIVERABLES:

- [ ] Complete Vue.js application
- [ ] All 18+ pages/components
- [ ] Routing setup (Vue Router)
- [ ] Authentication flow
- [ ] API integration
- [ ] Error handling
- [ ] Loading states
- [ ] Responsive design
- [ ] Tailwind styling
- [ ] Dockerfile (optional)
- [ ] README with setup instructions
- [ ] Example .env file
- [ ] Comments explaining components

================================================================================

DELIVERABLE INSTRUCTIONS:

1. Generate COMPLETE working Vue.js code
2. Code should run immediately with: npm install && npm run dev
   (or without build tools: just open index.html)
3. Include all pages and components
4. Add comprehensive comments
5. Make it responsive (mobile-friendly)
6. Include example API calls
7. Add error handling and validation
8. Create seed/demo data if needed
9. Include README with setup instructions

START GENERATION NOW.
```

---

# HOW TO USE THESE PROMPTS

## Timeline:

### NOW (This Week):
1. ✅ Copy **PROMPT 1: BACKEND API** (entire thing above)
2. ✅ Go to https://claude.ai or Anthropic API
3. ✅ Paste entire prompt
4. ✅ Wait for generation
5. ✅ Download all files
6. ✅ Test locally: `docker-compose up --build`
7. ✅ Verify API works at http://localhost:5000/api/v1/docs

### AFTER BACKEND WORKS (1-2 weeks):
1. ✅ Copy **PROMPT 2: FRONTEND** (entire thing above)
2. ✅ Go to Claude
3. ✅ Paste entire prompt
4. ✅ Download all Vue files
5. ✅ Place in `/frontend` folder
6. ✅ Test locally: `npm install && npm run dev`
7. ✅ Frontend at http://localhost:3000

### THEN (Integration):
1. ✅ Backend running at localhost:5000
2. ✅ Frontend running at localhost:3000
3. ✅ Login and test all features
4. ✅ Deploy both to AWS EC2

---

# CHECKLIST FOR USING PROMPTS

## Backend Prompt Checklist:
- [ ] Copy entire prompt
- [ ] Give to Claude
- [ ] Get complete backend code
- [ ] Extract to `/backend` folder
- [ ] Create `.env` file
- [ ] Run `docker-compose up --build`
- [ ] Test at http://localhost:5000/api/v1/docs
- [ ] Create test user accounts
- [ ] Test all endpoints work
- [ ] Check database has data

## Frontend Prompt Checklist:
- [ ] Copy entire prompt
- [ ] Give to Claude
- [ ] Get complete Vue code
- [ ] Extract to `/frontend` folder
- [ ] Create `.env` file (if needed)
- [ ] Run `npm install && npm run dev`
- [ ] Test at http://localhost:3000
- [ ] Login with test account
- [ ] Test all pages work
- [ ] Test API integration

## Deployment Checklist:
- [ ] Both backend and frontend work locally
- [ ] Update CORS in backend for production domain
- [ ] Create AWS resources (EC2, RDS, S3)
- [ ] Deploy backend to EC2
- [ ] Deploy frontend (build and serve)
- [ ] Test from external IP
- [ ] Set up domain with Route 53
- [ ] Enable HTTPS