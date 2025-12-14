'''
Configurações gerais usadas na aplicação.
'''
import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


load_dotenv()


class Settings(BaseSettings):
    '''
    Configurações gerais usadas na aplicação.
    '''
    API_V1_STR: str = "/api/v1"
    DB_URL: str = f'''postgresql+asyncpg:
                    //{os.getenv('DB_USER')}
                    :{os.getenv('DB_PASSWORD')}
                    @{os.getenv('DB_HOST')}
                    :{os.getenv('DB_PORT')}
                    /{os.getenv('DB_NAME')}'''
    DBBaseModel = declarative_base()

    class Config:
        '''
        Docstring for Config
        '''
        case_sensitive = True


setting = Settings()
