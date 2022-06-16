from apimain.Lib.func import connect
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from apimain.APIs.Auth import router
from apimain.Lib.client import *
from fastapi.templating import Jinja2Templates
from fastapi import WebSocket, WebSocketDisconnect
from typing import List


app=FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/')
def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()




@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"{username} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{username} left the chat")



app.include_router(router)

