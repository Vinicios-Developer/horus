from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.schemas.schemas import Produto, Usuario, ProdutoSimples
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario

# criando o banco de dados
# criar_db()

app = FastAPI()


@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


@app.post('/usuarios', status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado


@app.get('/usuarios', status_code=status.HTTP_200_OK)
def listar_usuario(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios
