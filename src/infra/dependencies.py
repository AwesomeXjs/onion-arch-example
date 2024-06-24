from fastapi import Depends
from infra.db.config.db_helper import db_helper
from infra.db.services.task_service import TaskRepository, TaskService


async def session_depends():
    async with db_helper.session_factory() as session:
        yield session
        await session.close()


def car_service(session=Depends(session_depends)):
    return TaskService(task_repo=TaskRepository, session=session)
