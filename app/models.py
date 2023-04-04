from pydantic import BaseModel
from typing import List, Optional


class ErrorResponse(BaseModel):
    name: Optional[str]
    message: Optional[str]
    code: Optional[int]


class ImageEmbeddingsResponseData(BaseModel):
    content_type: str
    embeddings: List[float]
    filename: str
    size: int


class ImageEmbeddingsResponse(BaseModel):
    error: Optional[ErrorResponse] = None
    data: Optional[ImageEmbeddingsResponseData] = None
