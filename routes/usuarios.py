from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas import usuarios as schemas_usuario 
from crud import usuarios as usuario_crud

router = APIRouter()

@router.get("/",response_model=List[schemas_usuario.UserBase])
def read_users(db: Session = Depends(get_db)):
    return usuario_crud.get_user(db=db)

@router.post("/", response_model=schemas_usuario.UserCreate)
def create_user(user: schemas_usuario.UserCreate, db: Session = Depends(get_db)):
    return usuario_crud.create_user(db=db, user=user)

@router.post("/login", response_model=schemas_usuario.UserOut)
def login_user(user: schemas_usuario.UserLogin, db: Session = Depends(get_db)):
    db_user = usuario_crud.login_user(db=db, correo=user.correo, contraseña=user.contraseña)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")

    return db_user