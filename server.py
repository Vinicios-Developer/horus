from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Animal(BaseModel):
    id: int
    nome: str
    idade: int
    sexo: str
    cor: str


banco: List[Animal] = []


@app.get('/animais')
def listar_animais():
    return banco


@app.post('/animais')
def criar_animal(animais: Animal):
    banco.append(animais)
    return None
