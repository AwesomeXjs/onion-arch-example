from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from infra.dependencies import task_service, get_task_by_id

from .schemas import TaskSchemaCreate, TaskSchema
from core.abc_service.task_service_abc import TaskServiceABC

router = APIRouter(prefix="/tasks")


@router.post("/")
async def create_task(
    task: TaskSchemaCreate,
    task_service: Annotated[TaskServiceABC, Depends(task_service)],
):
    try:
        await task_service.create_task(task=task)
        return {"status": "ok", "data": f"Таска '{task.title}' создана"}
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Такая таска уже существует",
        )


@router.get("/{id}")
async def get_task_by_id(task: Annotated[TaskSchema, Depends(get_task_by_id)]):
    return task
