'''
Docstring for schemas.curso_schema
'''
from typing import Optional
from pydantic import BaseModel as SCBaseModel


class CursoSchemaBase(SCBaseModel):
    '''
    Base schema for Curso
    '''
    titulo: str
    aulas: int
    horas: int


class CursoSchema(CursoSchemaBase):
    '''
    Schema for Curso response
    '''
    id: Optional[int] = None

    class Config:
        '''
        Docstring for Config
        '''
        from_attributes = True


class CursoSchemaCreate(CursoSchemaBase):
    '''
    Schema for Curso creation
    '''
    pass
