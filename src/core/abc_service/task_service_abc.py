from abc import ABC, abstractmethod

from core.entities.task import TaskDomain
from core.abc_repositories.task_repo_abc import TaskRepoABC
from core.abc_repositories.dto.task_dto import TaskCreateDto, TaskUpdateDto


class TaskServiceABC(ABC):
    def __init__(self, repository):
        self.repository: TaskRepoABC = repository

    @abstractmethod
    async def create_task(
        self,
        task: TaskCreateDto,
    ):
        return await self.repository.create_task()

    @abstractmethod
    async def find_task(
        self,
        id: int,
    ) -> TaskDomain:
        return await self.repository.find_task()

    @abstractmethod
    async def delete_task(
        self,
        id: int,
    ) -> TaskDomain:
        return await self.repository.delete_task()

    @abstractmethod
    async def update_task(
        self,
        task: TaskUpdateDto,
    ) -> TaskDomain:
        return await self.repository.update_task()
