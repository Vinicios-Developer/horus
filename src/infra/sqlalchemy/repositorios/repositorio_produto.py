from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioProduto():

    def __init__(self, db: Session):
        self.session = db

    def criar(self, produto: schemas.Produto, usuario_id: int):
        models.Produto.usuario_id = usuario_id
        db_produto = models.Produto(nome=produto.nome,
                                    detalhes=produto.detalhes,
                                    preco=produto.preco,
                                    disponivel=produto.disponivel,
                                    tamanho=produto.tamanho,
                                    usuario_id=usuario_id)
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto

    def listar(self, usuario_id: int):
        consulta = select(models.Produto).where(
            models.Produto.usuario_id == usuario_id)
        produtos = self.session.execute(consulta).scalars().all()
        return produtos

    def buscarPorId(self, produto_id: int, usuario_id: int):
        consulta = select(models.Produto).where(models.Produto.usuario_id == usuario_id, models.Produto.id == produto_id)
        produto = self.session.execute(consulta).first()
        return produto

    def editar(self, id: int, produto: schemas.Produto):
        update_stmt = update(models.Produto).where(
            models.Produto.id == id).values(nome=produto.nome,
                                            detalhes=produto.detalhes,
                                            preco=produto.preco,
                                            disponivel=produto.disponivel,
                                            tamanho=produto.tamanho)
        self.session.execute(update_stmt)
        self.session.commit()

    def remover(self, id: int):
        delete_stmt = delete(models.Produto).where(
            models.Produto.id == id
        )
        self.session.execute(delete_stmt)
        self.session.commit()
