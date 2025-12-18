'''
Docstring for api.v1.endpoints.curso
'''
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.curso_model import CursoModel
from schemas.curso_schema import CursoSchema, CursoSchemaCreate
from core.deps import get_session


router = APIRouter()


@router.post(
    '/',
    response_model=CursoSchema,
    status_code=status.HTTP_201_CREATED
)
async def post_curso(
    curso: CursoSchemaCreate,
    db: AsyncSession = Depends(get_session)
):
    '''
    Docstring for post_curso

    :param curso: Description
    :type curso: CursoSchema
    :param db: Description
    :type db: AsyncSession
    '''
    novo_curso = CursoModel(
        titulo=curso.titulo,
        aulas=curso.aulas,
        horas=curso.horas
    )
    db.add(novo_curso)
    await db.commit()
    return novo_curso


@router.get('/', response_model=List[CursoSchema])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    '''
    Docstring for get_cursos

    :param db: Description
    :type db: AsyncSession
    '''
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = list(result.scalars().all())
        return cursos


@router.get(
    '/{curso_id}',
    response_model=CursoSchema,
    status_code=status.HTTP_200_OK
)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    '''
    Docstring for get_curso

    :param curso_id: Description
    :type curso_id: int
    :param db: Description
    :type db: AsyncSession
    '''
    print('curso_id', curso_id)
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso: CursoModel | None = result.scalar_one_or_none()

        if curso:
            return curso
        else:
            raise HTTPException(
                detail='Curso não encontrado',
                status_code=status.HTTP_404_NOT_FOUND
            )


@router.put(
    '/{curso_id}',
    response_model=CursoSchema,
    status_code=status.HTTP_202_ACCEPTED
)
async def put_curso(
    curso_id: int,
    curso: CursoSchema,
    db: AsyncSession = Depends(get_session)
):
    '''
    Docstring for put_curso

    :param curso_id: Description
    :type curso_id: int
    :param curso: Description
    :type curso: CursoSchema
    :param db: Description
    :type db: AsyncSession
    '''
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_up: CursoModel | None = result.scalar_one_or_none()

        if curso_up:
            curso_up.titulo = curso.titulo  # type: ignore
            curso_up.aulas = curso.aulas  # type: ignore
            curso_up.horas = curso.horas  # type: ignore

            await session.commit()
            return curso_up
        else:
            raise HTTPException(
                detail='Curso não encontrado',
                status_code=status.HTTP_404_NOT_FOUND
            )


@router.delete(
    '/{curso_id}',
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_curso(
    curso_id: int,
    db: AsyncSession = Depends(get_session)
):
    '''
    Docstring for delete_curso

    :param curso_id: Description
    :type curso_id: int
    :param db: Description
    :type db: AsyncSession
    '''
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_del: CursoModel | None = result.scalar_one_or_none()

        if curso_del:
            await session.delete(curso_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(
                detail='Curso não encontrado',
                status_code=status.HTTP_404_NOT_FOUND
            )
