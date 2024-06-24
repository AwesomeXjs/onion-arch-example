from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from infra.db.config.db_helper import session_depends

from infra.controllers.api_v1 import router as v1_router


def create_app() -> FastAPI:
    """
    Фабрика FastAPI.
    """
    app = FastAPI(title="Onion architecture")

    app.include_router(v1_router)

    return app
