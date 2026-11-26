from models.usuarios import Usuarios  
from schemas import usuarios as schemas_usuario
from sqlalchemy.orm import Session
import bcrypt #Función para encriptar la contraseña del usuario antes de guardarla en la base de datos


def get_user(db: Session):
  return db.query(Usuarios).all()


def create_user(db: Session, user: schemas_usuario.UserCreate):

  hash_contraseña = bcrypt.hashpw(user.contraseña.encode(), bcrypt.gensalt()).decode()
  db_user = Usuarios(
    nombre=user.nombre, 
    correo=user.correo,
    contraseña=hash_contraseña,
    foto=user.foto,
    rol=user.rol,
    estado=user.estado
    )
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user



def login_user(db: Session, correo: str, contraseña: str):
    db_user = db.query(Usuarios).filter(Usuarios.correo == correo).first()
    if db_user is None:
        return None
    if not bcrypt.checkpw(contraseña.encode(), db_user.contraseña.encode()):
        return None
    return db_user


def update_user(db: Session, user_id: int, user: schemas_usuario.UserUpdate):
  db_user = db.query(Usuarios).filter(Usuarios.id == user_id).first()
  if db_user:
    db_user.nombre = user.nombre
    db_user.correo = user.correo
    db_user.contraseña = user.contraseña
    db_user.foto = user.foto
    db_user.rol = user.rol
    db_user.estado = user.estado
    db.commit()
    db.refresh(db_user)
  return db_user