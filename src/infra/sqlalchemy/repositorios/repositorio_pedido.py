from sqlalchemy import select
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioPedido():
    def __init__(self, session: Session):
        self.session = session

    def gravar_pedido(self, pedido: schemas.Pedido, usuario_id: int):
        models.Pedido.usuario_id = usuario_id
        pedido_db = models.Pedido(quantidade=pedido.quantidade,
                                  local_entrega=pedido.local_entrega,
                                  tipo_entrega=pedido.tipo_entrega,
                                  observacao=pedido.observacao,
                                  usuario_id=usuario_id,
                                  produto_id=pedido.produto_id)
        self.session.add(pedido_db)
        self.session.commit()
        self.session.refresh(pedido_db)
        return pedido_db

    def buscar_por_id(self, pedido_id: int, usuario_id: int) -> models.Pedido:
        consulta = select(models.Pedido).where(
            models.Pedido.usuario_id == usuario_id,
            models.Pedido.id == pedido_id
        )
        pedido = self.session.execute(consulta).scalars().one()
        return pedido

    def listar_meus_pedidos_por_usuario_id(self, usuario_id: int):
        consulta = select(models.Pedido).where(
            models.Pedido.usuario_id == usuario_id)
        pedidos = self.session.execute(consulta).scalars().all()
        return pedidos

    def listar_minhas_vendas_por_usuario_id(self, usuario_id: int):
        query = select(models.Pedido) \
            .join_from(models.Pedido, models.Produto) \
            .where(models.Produto.usuario_id == usuario_id)
        pedidos = self.session.execute(query).scalars().all()
        return pedidos
