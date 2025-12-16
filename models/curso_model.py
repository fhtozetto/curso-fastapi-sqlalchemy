'''
Docstring for models.curso_model
'''
from sqlalchemy import Column, Integer, String

from core.configs import DBBaseModel


class CursoModel(DBBaseModel):
    '''
    Docstring for CursoModel
    '''
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), unique=True, index=True, nullable=False)
    aulas = Column(Integer, nullable=False)
    horas = Column(Integer, nullable=False)
