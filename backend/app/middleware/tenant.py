from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from uuid import UUID

class TenantMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        tenant_id = request.headers.get("X-Tenant-ID")
        if tenant_id:
            try:
                request.state.tenant_id = UUID(tenant_id)
            except ValueError:
                request.state.tenant_id = None
        else:
            request.state.tenant_id = None
        
        response = await call_next(request)
        return response
