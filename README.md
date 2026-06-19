# Sahayta LMS

Sahayta is a modern, scalable Learning Management System (LMS) designed with a clean, professional aesthetic. It supports a multi-tenant architecture, dynamic course building, quizzes, and comprehensive student tracking.

## Technology Stack

- **Frontend**: Vue 3, Vite, Tailwind CSS, Pinia (State Management), Vue Router
- **Backend**: Python 3.10+, FastAPI, SQLAlchemy (SQLite/PostgreSQL), PyJWT, Passlib
- **Infrastructure as Code**: Terraform
- **Configuration Management**: Ansible
- **CI/CD**: GitHub Actions
- **Hosting**: AWS (S3 for Frontend, EC2 for Backend & Database)

---

## Architecture Overview

To ensure maximum cost-efficiency while maintaining a professional deployment architecture, Sahayta utilizes a hybrid deployment model:

1. **Static Frontend**: The Vue.js application is compiled into static HTML/CSS/JS and hosted directly on an **Amazon S3 Bucket** configured for static web hosting. This ensures lightning-fast load times and infinite scalability at almost zero cost.
2. **Backend Monolith**: The FastAPI backend and the database (PostgreSQL via Docker) are hosted together on a single **AWS EC2 `t3.micro` instance**. This keeps the infrastructure entirely within the AWS Free Tier while still supporting containerized, modern application standards.

---

## CI/CD Pipeline Setup

Sahayta features a 100% automated Continuous Integration and Continuous Deployment (CI/CD) pipeline powered by GitHub Actions, Terraform, and Ansible. 

### 1. Infrastructure Provisioning (Terraform)
All AWS infrastructure is defined as code in the `infrastructure/terraform` directory. 
Running `terraform apply` automatically creates:
- A Virtual Private Cloud (VPC) and Subnets.
- Security Groups (allowing ports 80, 443, 22, and 5000).
- An EC2 Instance for the backend.
- An S3 Bucket for the frontend.
- An RSA SSH Key Pair (`lms-terraform-key.pem`) for server access.

### 2. Configuration Management (Ansible)
Server configuration is handled by Ansible (`infrastructure/ansible/playbook.yml`). You do not need to run Ansible manually! The GitHub Actions pipeline automatically runs this playbook on the EC2 server during deployment to:
- Install Docker and Docker-Compose.
- Create necessary application directories (`/opt/lms-backend`).
- Configure user permissions.

### 3. Automated Deployments (GitHub Actions)
Whenever code is pushed to the `main` branch, GitHub Actions automatically takes over.

**Frontend Workflow (`deploy-frontend.yml`)**:
- Triggers when files in `frontend/` change.
- Installs Node.js dependencies.
- Runs `npm run build` to compile the Vue app.
- Uses the AWS CLI to sync the compiled `dist/` folder directly to the S3 bucket.

**Backend Workflow (`deploy-backend.yml`)**:
- Triggers when files in `backend/` change.
- Installs Ansible on the GitHub Runner.
- Connects to the EC2 server and runs the Ansible playbook to ensure Docker is installed.
- Securely copies (`scp`/`rsync`) the Python backend code to the server.
- Runs `docker-compose down && docker-compose up -d --build` to reboot the FastAPI and Database containers with the latest code.

---

## Developer Guide: Recreating the Infrastructure

If you ever destroy the AWS infrastructure (via `terraform destroy`) and need to recreate it, follow these steps to restore the CI/CD pipeline:

1. Navigate to `infrastructure/terraform` and run:
   ```bash
   terraform apply
   ```
2. Note the **Public IP Address** and **S3 Bucket URL** outputted by Terraform.
3. Update the `API_BASE_URL` in `frontend/src/api.js` to point to `http://<NEW_EC2_IP>:5000/api/v1`.
4. Go to your GitHub Repository -> Settings -> Secrets and Variables -> Actions.
5. Update the following secrets:
   - `EC2_HOST`: The new IP address of the EC2 instance.
   - `EC2_SSH_KEY`: The complete contents of the newly generated `lms-terraform-key.pem` file.
   - `S3_BUCKET_NAME`: The name of the new S3 bucket.
6. Push your code to GitHub. The CI/CD pipeline will automatically configure the blank server, install Docker, and deploy the application!
