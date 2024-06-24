from abc import ABC, abstractmethod

from core.entities.task import TaskDomain
from .dto.task_dto import TaskCreateDto, TaskUpdateDto


class TaskRepoABC(ABC):

    @abstractmethod
    async def create_task(task: TaskCreateDto):
        raise NotImplementedError

    @abstractmethod
    async def find_task(id: int) -> TaskDomain:
        raise NotImplementedError

    @abstractmethod
    async def delete_task(id: int) -> TaskDomain:
        raise NotImplementedError

    @abstractmethod
    async def update_task(task: TaskUpdateDto) -> TaskDomain:
        raise NotImplementedError
