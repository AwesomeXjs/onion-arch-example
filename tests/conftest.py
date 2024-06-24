from fastapi import FastAPI
from typing import AsyncGenerator
from httpx import ASGITransport, AsyncClient

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from main import create_app
from infra.db.models import Base
from infra.db.config import settings
from infra.db.config.db_helper import DatabaseHelper, session_depends


TEST_DB_URL = settings.db_url_test
db_helper_test = DatabaseHelper(url=TEST_DB_URL, echo=True)


async def override_session_depends():
    async with db_helper_test.session_factory() as session:
        yield session
        await session.close()


@pytest.fixture(scope="session", autouse=True)
async def create_tables():
    async with db_helper_test.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    # async with engine_test.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    app: FastAPI = create_app()
    app.dependency_overrides[session_depends] = override_session_depends
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac
