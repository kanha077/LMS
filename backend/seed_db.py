import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.tenant import Tenant
from app.models.user import User, UserRole
from app.models.course import Course
from app.models.assignment import Assignment
from app.models.course_enrollment import CourseEnrollment
from app.security import get_password_hash
from datetime import datetime, timedelta

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://lms_user:secure_password@postgres:5432/student_lms")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

def seed_database():
    print("Starting database seeding...")
    
    # 1. Create a Tenant
    tenant = db.query(Tenant).filter(Tenant.name == "Global Tech University").first()
    if not tenant:
        tenant = Tenant(name="Global Tech University", subdomain="globaltech")
        db.add(tenant)
        db.commit()
        db.refresh(tenant)
        print("Created Tenant: Global Tech University")

    # 2. Create Admin
    admin_email = "admin@test.com"
    admin = db.query(User).filter(User.email == admin_email).first()
    if not admin:
        admin = User(
            tenant_id=tenant.id,
            email=admin_email,
            password_hash=get_password_hash("test123"),
            full_name="System Admin",
            role=UserRole.admin
        )
        db.add(admin)
        print("Created Admin: admin@test.com")

    # 3. Create Teacher (User's requested account)
    teacher_email = "test@mail"
    teacher = db.query(User).filter(User.email == teacher_email).first()
    if not teacher:
        teacher = User(
            tenant_id=tenant.id,
            email=teacher_email,
            password_hash=get_password_hash("test123"),
            full_name="Dr. Test Teacher",
            role=UserRole.teacher
        )
        db.add(teacher)
        db.commit()
        db.refresh(teacher)
        print(f"Created Teacher: {teacher_email} (Password: test123)")

    # 4. Create Student
    student_email = "student@test.com"
    student = db.query(User).filter(User.email == student_email).first()
    if not student:
        student = User(
            tenant_id=tenant.id,
            email=student_email,
            password_hash=get_password_hash("test123"),
            full_name="Alice Student",
            role=UserRole.student
        )
        db.add(student)
        db.commit()
        db.refresh(student)
        print("Created Student: student@test.com")

    # 5. Create a Course
    course = db.query(Course).filter(Course.code == "CS101").first()
    if not course:
        course = Course(
            tenant_id=tenant.id,
            name="Introduction to Computer Science",
            description="A comprehensive intro to programming.",
            code="CS101",
            teacher_id=teacher.id,
            semester="Fall 2026"
        )
        db.add(course)
        db.commit()
        db.refresh(course)
        print("Created Course: CS101")

    # 6. Enroll Student
    enrollment = db.query(CourseEnrollment).filter(CourseEnrollment.course_id == course.id, CourseEnrollment.student_id == student.id).first()
    if not enrollment:
        enrollment = CourseEnrollment(
            tenant_id=tenant.id,
            course_id=course.id,
            student_id=student.id,
            grade="A",
            status="active"
        )
        db.add(enrollment)
        print("Enrolled Alice in CS101")

    # 7. Create Assignment
    assignment = db.query(Assignment).filter(Assignment.course_id == course.id).first()
    if not assignment:
        assignment = Assignment(
            tenant_id=tenant.id,
            course_id=course.id,
            title="Homework 1: Hello World",
            description="Write a program that prints Hello World",
            instructions="Submit a Python file.",
            due_date=datetime.utcnow() + timedelta(days=7),
            total_points=100,
            created_by=teacher.id,
            is_published=True
        )
        db.add(assignment)
        print("Created Assignment: Homework 1")

    db.commit()
    print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed_database()
