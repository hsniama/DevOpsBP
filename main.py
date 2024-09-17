from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI();

API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"

class Message(BaseModel):
    message: str
    to: str
    from_: str
    timeToLifeSec: int


@app.post("/DevOps")
async def devops(message: Message, x_parse_rest_api_key: str = Header(...)):
    if x_parse_rest_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="No Autorizado")

    return {"message": f"Hello {message.to} your message will be send"}

@app.get("/{path}")
async def handle_invalid_method():
    return "ERROR"

@app.put("/{path}")
async def handle_invalid_method():
    return "ERROR"

@app.delete("/{path}")
async def handle_invalid_method():
    return "ERROR"