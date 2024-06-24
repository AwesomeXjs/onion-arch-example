from typing import Annotated

from fastapi import Depends
from infra.db.config.db_helper import db_helper
from core.abc_service.task_service_abc import TaskServiceABC
from infra.db.services.task_service import TaskRepository, TaskService


async def session_depends():
    async with db_helper.session_factory() as session:
        yield session
        await session.close()


def task_service(session=Depends(session_depends)):
    return TaskService(task_repo=TaskRepository, session=session)


async def get_task_by_id(
    id: int, task_service: Annotated[TaskServiceABC, Depends(task_service)]
):
    return await task_service.find_task(id=id)
