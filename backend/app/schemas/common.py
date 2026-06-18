from pydantic import BaseModel
from typing import Generic, TypeVar, List, Optional
from uuid import UUID

T = TypeVar('T')

class Pagination(BaseModel):
    total: int
    page: int
    page_size: int
    total_pages: int

class PaginatedResponse(BaseModel, Generic[T]):
    success: bool = True
    data: List[T]
    pagination: Pagination

class SuccessResponse(BaseModel, Generic[T]):
    success: bool = True
    data: T
    message: str = "Operation successful"

class ErrorDetail(BaseModel):
    field: str
    message: str

class ErrorResponse(BaseModel):
    success: bool = False
    error: str
    message: str
    details: Optional[List[ErrorDetail]] = None
