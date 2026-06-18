from .auth import router as auth_router
from .users import router as users_router
from .courses import router as courses_router
from .assignments import router as assignments_router
from .submissions import router as submissions_router
from .tenant import router as tenant_router

routers = [
    auth_router,
    users_router,
    courses_router,
    assignments_router,
    submissions_router,
    tenant_router
]
