"""
Pydantic models for validating post data.
"""

from pydantic import BaseModel


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class PostSummarySchema(BaseModel):
    userId: int
    post_count: int
