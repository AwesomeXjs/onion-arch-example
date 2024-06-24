from pydantic import BaseModel

from core.entities.task import TaskDomain
from core.abc_repositories.dto.task_dto import TaskCreateDto, TaskUpdateDto


class TaskSchema(TaskDomain, BaseModel):
    pass


class TaskSchemaCreate(TaskCreateDto, BaseModel):
    pass


class TaskSchemaUpdate(TaskUpdateDto, BaseModel):
    pass
