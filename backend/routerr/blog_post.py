from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix = "/blog",
    tags = ["blog"]
)

class BlogModel(BaseModel):
    title: str
    content: str
    number: int
    published: Optional [bool] = True

@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 2):
    return {
        "id": id,
        "data": blog,
        "version": version
        }
