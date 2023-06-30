from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_produtos, rotas_usuarios

# criando o banco de dados
# criar_db()

app = FastAPI()

# CORS
origins = ['http://127.0.0.1:8000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(rotas_produtos.router)

app.include_router(rotas_usuarios.router)
