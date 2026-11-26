from pydantic import BaseModel

#DAMOS FORMATO A LOS DATOS QUE SE VAN A ENVIAR Y RECIBIR DE LA API
class UserBase(BaseModel):
  nombre: str
  correo: str
  contraseña: str
  foto: bytes
  rol: int
  estado: bool

#Finalmente, definimos los modelos de respuesta y creación de usuario, heredando de UserBase. Esto nos permite reutilizar los campos comunes y mantener un código más limpio y organizado.
class UserResponse(UserBase):
  id: int

  class Config:
    from_attributes = True

#Clase para la creación de un usuario, heredando de UserBase. Esto nos permite reutilizar los campos comunes y mantener un código más limpio y organizado.
class UserCreate(UserBase):
  pass

#Clase para la actualización de un usuario, heredando de UserBase. Esto nos permite reutilizar los campos comunes y mantener un código más limpio y organizado.
class UserUpdate(UserBase):
  pass

#Clase para la eliminación de un usuario, heredando de BaseModel. Esto nos permite definir solo el campo necesario para la eliminación, que es el id del usuario.
class UserDelete(BaseModel):
  id: int


#Clase para el inicio de sesión de un usuario, heredando de BaseModel. Esto nos permite definir solo los campos necesarios para el inicio de sesión, que son el correo y la contraseña.
class UserLogin(BaseModel):
  correo: str
  contraseña: str

class UserOut(BaseModel):        # lo que SALE
  id: int
  correo: str
  rol: int
  model_config = {"from_attributes": True}