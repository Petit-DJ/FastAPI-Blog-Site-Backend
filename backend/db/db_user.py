from fastapi import HTTPException
from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
import bcrypt

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = bcrypt.hashpw(request.password.encode("utf-8"),  bcrypt.gensalt())
    )

    db.add(new_user) # add user
    db.commit() # sends op to db
    db.refresh(new_user)  
    return new_user
 
def get_all_users(db:Session):
    # return db.query(DbUser).all()
    return db.query(DbUser).filter(DbUser.id==id).first()

def get_one_user(db:Session, id: int):
    return db.query(DbUser).filter(DbUser.id==id).first()

#update user
def update_user( db: Session, id: int, request: UserBase):
    
    user = db.query(DbUser).filter(DbUser.id==id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password : bcrypt.hashpw(request.password.encode("utf-8"),  bcrypt.gensalt())
    })
    db.commit()
    return db.query(DbUser).filter(DbUser.id == id).first()

def delete_user(db:Session, id:int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}
    
    # users = db.query(DbUser).filter(DbUser.id==id).first()
    # db.delete(users)
    # db.commit()
    # return db.query(DbUser).filter(DbUser.id == id).first()
