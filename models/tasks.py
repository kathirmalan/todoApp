from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task: str
    completed: str
    status: str
    created_date: str
    due_date: Optional[str] = None
