from app.database import Base
from .tenant import Tenant
from .user import User
from .course import Course
from .course_enrollment import CourseEnrollment
from .assignment import Assignment
from .submission import Submission
from .attendance import Attendance
from .audit_log import AuditLog

# Phase 1: New Models
from .lesson import Lesson, LessonModule
from .quiz import Quiz, QuizQuestion, QuizOption, QuizAttempt, Grade
from .discussion import DiscussionBoard, DiscussionPost, DiscussionReply
from .resource import Resource
from .messaging import Message, Notification, Announcement
from .gamification import Badge, UserBadge
from .study_group import StudyGroup, StudyGroupMember
from .note import Note
from .subscription import SubscriptionTier
from .calendar import CalendarEvent
