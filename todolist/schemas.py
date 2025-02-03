from pydantic import BaseModel


"""базовая схема задачи"""
class TaskBase(BaseModel):
    title: str
    description: str = None
    completed: bool = None

"""Схема для создания задач"""

class TaskCreate(TaskBase):
    pass

"""Схема для отображения задач"""
class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
