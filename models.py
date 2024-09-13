from typing import Optional
from pydantic import BaseModel

class Task(BaseModel):
    id: Optional[int] = None
    task: str
    completed: bool = False