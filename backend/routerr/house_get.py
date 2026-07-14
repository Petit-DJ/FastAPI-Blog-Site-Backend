from fastapi import APIRouter, Response, status
from enum import Enum
from typing import Optional

router = APIRouter(
    prefix='/house',
    tags = ['house']
)


@router.get(
    '/all',
    summary = "Call all houses",
    description = "api call simulates calling all houses",
)
def get_houses(floor= 2, classes: Optional[str] = None):
    return {'message': f'All {classes} houses on floor {floor}'}

@router.get("/{id}/students/{student_id}", tags= ["Students"])
def get_student(id: int, student_id:int, valid: bool = True, username: Optional [str] = None):

    """
    Simulates retrieving a student of a house
    - **id** mandatory path parameter
    - **student_id** mandatory path parameter
    - **bool** optional query parameter
    - **username** optional query parameter
    """
    return {'message': f'house_id {id}, student_id {student_id}, valid {valid}, username {username}'}

class HouseType(str, Enum):
    red = "Gryfinndor"
    green = "Slytherin"
    yellow = "Hupplepuff"
    blue = "Ravenclaw"

@router.get("/type/{type}")
def get_house_type(type: HouseType):
    return {"message": f"House type {type}"}

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
  if id > 5:
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': f'Blog {id} not found'}
  else : 
    response.status_code = status.HTTP_200_OK
    return {'message': f'Blog with id {id}'}