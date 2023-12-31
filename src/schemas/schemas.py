from pydantic import BaseModel
from typing import Optional, List


class ProdutoSimples(BaseModel):
    nome: str
    id: Optional[int] = None
    preco: float
    disponivel: bool

    class Config:
        orm_mode = True


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    produtos: List[ProdutoSimples] = []

    class Config:
        orm_mode = True


class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class Config:
        orm_mode = True


class LoginData(BaseModel):
    senha: str
    telefone: str


class LoginSucesso(BaseModel):
    usuario: UsuarioSimples
    access_token: str


class Produto(BaseModel):
    nome: str
    id: Optional[int] = None
    detalhes: str
    preco: float
    disponivel: bool = False
    tamanho: str
    usuario_id: Optional[int]
    usuario: Optional[UsuarioSimples]

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[int] = None
    quantidade: int
    local_entrega: Optional[str]
    tipo_entrega: str
    observacao: Optional[str] = 'Sem observações'
    usuario_id: Optional[int]
    produto_id: Optional[int]

    usuario: Optional[UsuarioSimples]
    produto: Optional[ProdutoSimples]

    class Config:
        orm_mode = True
