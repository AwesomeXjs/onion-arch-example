from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from core.abc_repositories.task_repo_abc import TaskRepoABC
from core.abc_repositories.dto.task_dto import TaskCreateDto


class SqlAlchemyRepository(TaskRepoABC):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_task(self, task: TaskCreateDto):
        stmt = insert(self.model).values(**task)
        await self.session.execute(stmt)

    async def delete_task(self):
        pass

    async def find_task(self):
        pass

    async def update_task(self):
        pass
