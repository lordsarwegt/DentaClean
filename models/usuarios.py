from sqlalchemy import BigInteger, Column, String, SmallInteger
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.dialects.mssql import BINARY
from motor_de_conexion import Base


class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    correo = Column(String(255), nullable=False)
    contraseña = Column(String(255), nullable=False)
    foto = Column(BINARY(16), nullable=False)
    rol = Column(String(255), nullable=False)
    estado = Column(TINYINT, nullable=False)
