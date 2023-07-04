from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido
from src.routers.auth_utils import obter_usuario_logado
from src.schemas.schemas import Pedido, Usuario

router = APIRouter()


@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedido(pedido: Pedido, usuario: Usuario = Depends(obter_usuario_logado), session: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(
        session).gravar_pedido(pedido, usuario.id)
    return pedido_criado


@router.get('/pedidos/{id}', response_model=Pedido)
def exibir_pedido(id: int, usuario: Usuario = Depends(obter_usuario_logado), session: Session = Depends(get_db)):
    try:
        pedido_localizado = RepositorioPedido(
            session).buscar_por_id(id, usuario.id)
        return pedido_localizado
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Pedido {id} inexistente')


@router.get('/pedidos', response_model=List[Pedido])
def listar_pedidos(usuario: Usuario = Depends(obter_usuario_logado), session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(
        session).listar_meus_pedidos_por_usuario_id(usuario.id)
    return pedidos


@router.get('/vendas',  response_model=List[Pedido])
def listar_vendas(usuario: Usuario = Depends(obter_usuario_logado), session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(
        session).listar_minhas_vendas_por_usuario_id(usuario.id)
    return pedidos
