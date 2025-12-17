'''
Docstring for schemas.curso_schema
'''
from typing import Optional
from pydantic import BaseModel as SCBaseModel


class CursoSchema(SCBaseModel):
    '''
    Docstring for CursoSchema
    '''
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int

    class Config:
        '''
        Docstring for Config
        '''
        orm_mode = True
