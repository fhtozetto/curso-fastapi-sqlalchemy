'''
Docstring for core.database
'''
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine

from core.configs import setting


engine: AsyncEngine = create_async_engine(
    setting.DB_URL,
    echo=True,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10
)


Session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)
