import uuid
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, func, Text
from sqlalchemy import Uuid as UUID
from app.database import Base

class Quiz(Base):
    __tablename__ = "quizzes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lesson_id = Column(UUID(as_uuid=True), ForeignKey("lessons.id"), nullable=True)
    title = Column(String(255), nullable=False)
    time_limit_minutes = Column(Integer, nullable=True)
    max_attempts = Column(Integer, default=1)
    passing_score = Column(Integer, default=50)
    shuffle_questions = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())

class QuizQuestion(Base):
    __tablename__ = "quiz_questions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    quiz_id = Column(UUID(as_uuid=True), ForeignKey("quizzes.id"), nullable=False)
    question_type = Column(String(50), nullable=False) # single, multi, true_false, short
    text = Column(Text, nullable=False)
    points = Column(Integer, default=1)
    order_index = Column(Integer, default=0)

class QuizOption(Base):
    __tablename__ = "quiz_options"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_id = Column(UUID(as_uuid=True), ForeignKey("quiz_questions.id"), nullable=False)
    text = Column(String(255), nullable=False)
    is_correct = Column(Boolean, default=False)

class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    quiz_id = Column(UUID(as_uuid=True), ForeignKey("quizzes.id"), nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    score = Column(Integer, nullable=True)
    is_passed = Column(Boolean, nullable=True)
    started_at = Column(DateTime, default=func.now())
    completed_at = Column(DateTime, nullable=True)

class Grade(Base):
    __tablename__ = "grades"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    assignment_id = Column(UUID(as_uuid=True), ForeignKey("assignments.id"), nullable=True)
    quiz_id = Column(UUID(as_uuid=True), ForeignKey("quizzes.id"), nullable=True)
    score = Column(Integer, nullable=False)
    max_score = Column(Integer, nullable=False)
    feedback = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())
