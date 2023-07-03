from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario, UsuarioSimples
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.providers import hash_provider

router = APIRouter()


@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuarioSimples)
def signup(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_localizado = RepositorioUsuario(
        session).obter_por_telefone(usuario.telefone)

    if usuario_localizado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Telefone já cadastrado')

    usuario.senha = hash_provider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado
