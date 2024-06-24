from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from infra.dependencies import car_service

from .schemas import TaskSchemaCreate
from core.abc_service.task_service_abc import TaskServiceABC

router = APIRouter(prefix="/tasks")


@router.post("/")
async def create_task(
    task: TaskSchemaCreate,
    task_service: Annotated[TaskServiceABC, Depends(car_service)],
):
    try:
        await task_service.create_task(task=task)
        return {"status": "ok", "data": "Таска '{task.title}' создана"}
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Такая таска уже существует",
        )
