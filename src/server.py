from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_auth, rotas_produtos, rotas_pedidos
from src.jobs.write_notification import write_notification

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

@app.post('/send_email/{email}')
def send_email(email: str, background: BackgroundTasks):
    background.add_task(write_notification, email, 'Vai, mano!')
    return {"Ok": "Mensagem enviada..."}

@app.middleware('http')
async def processar_tempo_requisicao(request: Request, next):
    print('Interceptou a chegada...')

    response = await next(request)

    print('Interceptou a volta...')

    return response
