from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional
import jwt

app = FastAPI()

API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"
JWT_SECRET = "1720844446"

class Message(BaseModel):
    message: str
    to: str
    from_: str
    timeToLifeSec: int

def verify_jwt(token: str):
    try:
        # Decodifica y valida el JWT
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="JWT expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid JWT")

@app.post("/DevOps")
async def devops(message: Message, x_parse_rest_api_key: str = Header(...), x_jwt_kwy: Optional[str] = Header(None)):
    # Verificamos la clave API
    if x_parse_rest_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    # Verificamos el JWT
    if x_jwt_kwy is None:
        raise HTTPException(status_code=401, detail="JWT required")
    
    verify_jwt(x_jwt_kwy)

    return {"message": f"Hello {message.to} your message will be send"}

@app.get("/{path}")
@app.put("/{path}")
@app.delete("/{path}")
async def handle_invalid_method():
    return "ERROR metodo diferente a POST"
