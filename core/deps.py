'''
Docstring for core.deps
'''
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Session


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    '''
    Docstring for get_session
    '''
    session: AsyncSession = Session()
    try:
        yield session
    finally:
        await session.close()
