from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = '967621f36d52a8b15500427513cde9e6'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000


def criar_access_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    dados.update({'exp': expiracao})

    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verificar_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get('sub')
