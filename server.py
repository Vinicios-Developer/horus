from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cadastro(BaseModel):
    nome: str
    CPF: str
    email: str
    senha: str


@app.post('/cadastro')
def cadastro_user(cadastro: Cadastro):
    return {"mensagem": f"usuário {cadastro.nome} cadastrado com sucesso no HORUS!"}
