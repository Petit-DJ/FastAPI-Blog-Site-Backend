from fastapi import FastAPI, APIRouter, Request, Response
from routerr import blog_post
from db import models

from db.database import engine
from routerr import user, article, product, file
import os
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from auth import authentication
from client import html
from fastapi.websockets import WebSocket

rakesh = FastAPI()
# rakesh.include_router(house_get.router)
rakesh.include_router(blog_post.router)
rakesh.include_router(file.router)
rakesh.include_router(user.router)
rakesh.include_router(article.router)
rakesh.include_router(product.router)
rakesh.include_router(authentication.router)


@rakesh.get("/hello")
def hello():
    return {"message": "Hello, World!"}

origins = ['http://localhost:3000' ]

@rakesh.get("/")
async def get():
    return HTMLResponse(html)

clients =[]

@rakesh.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
       data = await websocket.receive_text()
       for client in clients:
          await client.send_text(data)
    

rakesh.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"] 
)
models.Base.metadata.create_all(engine)