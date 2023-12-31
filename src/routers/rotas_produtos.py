from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from src.schemas.schemas import Produto, ProdutoSimples, Usuario
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.routers.auth_utils import obter_usuario_logado

router = APIRouter()


@router.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
def criar_produto(produto: Produto, usuario: Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto, usuario.id)
    return produto_criado


@router.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[ProdutoSimples])
def listar_produtos(usuario: Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar(usuario.id)
    return produtos


@router.get('/produtos/{id}')
def exibir_produto(id: int, usuario: Usuario = Depends(obter_usuario_logado), session: Session = Depends(get_db)):
    produto_localizado = RepositorioProduto(
        session).buscarPorId(id, usuario.id)
    if produto_localizado is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Produto não encontrado com o id {id}")
    return produto_localizado._asdict()


@router.put('/produtos/{id}', response_model=ProdutoSimples)
def atualizar_produto(id: int, produto: Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(id, produto)
    produto.id = id
    return produto


@router.delete('/produtos/{id}')
def remover_produto(id: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return
