from typing import Optional, List
from sqlmodel import SQLModel, Field
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.types import JSON

class BlogPost(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    category: str
    tags: List[str] = Field(
        default_factory=list,
        sa_column=Column(JSON)
    )

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory= datetime.utcnow)
