# Multi-Tenant Learning Management System (LMS)

A robust, full-stack, multi-tenant Educational Learning Management System built from the ground up. This system is designed to allow multiple independent schools/organizations (tenants) to operate on a single shared backend infrastructure while keeping their data securely isolated.

## 🚀 Tech Stack

### Backend
* **Framework**: FastAPI (Python)
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy
* **Authentication**: JWT (JSON Web Tokens) with OAuth2
* **Infrastructure**: Docker & Docker Compose

### Frontend
* **Framework**: Vue 3 (Composition API)
* **Build Tool**: Vite
* **Styling**: Tailwind CSS v3
* **State Management**: Pinia
* **Routing**: Vue Router

---

## 🎯 Key Features

1. **True Multi-Tenancy**: Organizations can dynamically register. The system assigns them a unique subdomain and logically isolates their users, courses, and assignments in the PostgreSQL database using `tenant_id` foreign keys.
2. **Role-Based Dashboards**: 
   * **Students**: Can view enrolled courses, submit assignments, and track their GPA.
   * **Teachers**: Can create courses, publish assignments, and grade student submissions.
   * **Admins**: Can view system-wide analytics, tenant health, and manage users.
3. **Automated Database Seeding**: A built-in Python script to instantly populate the database with mock tenants, users, and courses for testing.

---

## 📂 Project Structure

The project is split into two completely decoupled repositories/folders:

```text
/
├── backend/                  # FastAPI Application
│   ├── app/
│   │   ├── models/           # SQLAlchemy Database Entities (Tenant, User, Course, etc.)
│   │   ├── routes/           # API Endpoints (Auth, Users, Courses, Assignments)
│   │   ├── schemas/          # Pydantic Models for Input Validation
│   │   ├── middleware/       # Custom middleware (e.g., Tenant isolation)
│   │   └── security.py       # Password hashing and JWT generation
│   ├── alembic/              # Database Migration scripts
│   ├── seed_db.py            # Python script to seed mock data
│   └── docker-compose.yml    # Docker configuration for FastAPI & PostgreSQL
│
└── frontend/                 # Vue 3 Application
    ├── src/
    │   ├── components/       # Reusable Vue components (Navbar, Sidebar, Spinner, Alerts)
    │   ├── pages/            # View components (Dashboards, Auth, Courses, Admin)
    │   ├── stores/           # Pinia State Management (auth.js)
    │   ├── api.js            # Axios client with JWT interceptors
    │   └── router.js         # Vue Router configuration & Auth Guards
    ├── tailwind.config.js    # Tailwind CSS Configuration
    └── vite.config.js        # Vite bundler configuration
```

---

## 🛠️ Installation & Setup Guide

To run this project locally, you will need **Docker Desktop** and **Node.js** installed on your machine.

### 1. Start the Backend (Docker)
The backend is fully containerized. Docker will automatically spin up the PostgreSQL database, run the Alembic migrations, and start the FastAPI server on port `5000`.

```bash
cd backend
docker-compose up --build
```
*The API will now be available at `http://localhost:5000`*

### 2. Start the Frontend
Open a **new** terminal window, navigate to the frontend directory, install the NPM packages, and start the Vite development server.

```bash
cd frontend
npm install
npm run dev
```
*The Web Application will now be available at `http://localhost:3001`*

### 3. Seed the Database
To easily test the application without manually registering a bunch of accounts, you can run the provided database seeder script. While the backend Docker container is running, open a terminal and run:

```bash
cd backend
docker exec lms_backend python seed_db.py
```

### 4. Test the Application
You can now log in at `http://localhost:3001` using any of the seeded accounts to explore the different role-based views!

**Teacher Account** (Creates courses & assignments):
* **Email**: `test@mail`
* **Password**: `test123`

**Student Account** (Views courses & submits work):
* **Email**: `student@test.com`
* **Password**: `test123`

**Admin Account** (System-wide analytics):
* **Email**: `admin@test.com`
* **Password**: `test123`
