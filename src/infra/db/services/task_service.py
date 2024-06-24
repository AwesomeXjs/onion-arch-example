from infra.db.models import Task
from core.entities.task import TaskDomain
from core.abc_repositories.task_repo_abc import TaskRepoABC
from core.abc_repositories.dto.task_dto import TaskCreateDto
from core.abc_service.task_service_abc import TaskServiceABC
from infra.db.repositories.sqlalchemy_repository import SqlAlchemyRepository


class TaskRepository(SqlAlchemyRepository):
    model = Task


class TaskService(TaskServiceABC):
    def __init__(self, task_repo, session):
        self.repo: TaskRepoABC = task_repo(session)
        self.session = session

    async def create_task(self, task: TaskCreateDto):
        task = task.model_dump()
        await self.repo.create_task(task)
        await self.session.commit()

    async def delete_task(self, id: int):
        pass

    async def find_task(self, **filter_by) -> TaskDomain:
        task = await self.repo.find_task(**filter_by)
        return task

    async def update_task(self):
        pass
