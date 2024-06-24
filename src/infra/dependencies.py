from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from infra.db.config.db_helper import session_depends
from core.abc_service.task_service_abc import TaskServiceABC
from infra.db.services.task_service import TaskRepository, TaskService


def task_service(session: Annotated[AsyncSession, Depends(session_depends)]):
    return TaskService(task_repo=TaskRepository, session=session)


async def get_task_by_id(
    id: int, task_service: Annotated[TaskServiceABC, Depends(task_service)]
):
    return await task_service.find_task(id=id)
