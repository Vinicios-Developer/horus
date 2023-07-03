from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_auth, rotas_produtos, rotas_pedidos

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

# Rota SEGURANÇA: Autenticação e Autorização
app.include_router(rotas_auth.router, prefix='/auth')

app.include_router(rotas_pedidos.router)
