from typing import List
from sqlmodel import SQLModel

class BlogPostCreate(SQLModel):
    title: str
    content: str
    category: str
    tags: List[str]

class BlogPostUpdate(SQLModel):
    title: str
    content: str
    category: str
    tags: List[str]
