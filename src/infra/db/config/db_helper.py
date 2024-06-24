from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from infra.db.config.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
        )


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=True,
)
