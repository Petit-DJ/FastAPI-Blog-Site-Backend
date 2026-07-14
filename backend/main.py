from fastapi import FastAPI, APIRouter, Request
from routerr import blog_post
from db import models
from db.database import engine
from routerr import user, article, product
import os
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from auth import authentication

rakesh = FastAPI()
# rakesh.include_router(house_get.router)
rakesh.include_router(blog_post.router)
rakesh.include_router(user.router)
rakesh.include_router(article.router)
rakesh.include_router(product.router)
rakesh.include_router(authentication.router)


@rakesh.get("/hello")
def hello():
    return {"message": "Hello, World!"}

origins = ['http://localhost:3000' ]

rakesh.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"] 
)
models.Base.metadata.create_all(engine)