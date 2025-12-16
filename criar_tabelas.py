'''
Docstring for criar_tabelas
'''
from core.configs import DBBaseModel
from core.database import engine


async def criar_tabelas() -> None:
    '''
    Docstring for criar_tabelas
    '''
    import models.__all_models
    print('Criando tabelas no banco de dados')

    async with engine.begin() as conn:
        await conn.run_sync(DBBaseModel.metadata.drop_all)
        await conn.run_sync(DBBaseModel.metadata.create_all)


if __name__ == '__main__':
    import asyncio
    asyncio.run(criar_tabelas())
