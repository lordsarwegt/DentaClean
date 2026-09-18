from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.dialects.mssql import BINARY
from motor_de_conexion import Base


class Clientes(Base):
    __tablename__ = "clientes"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    apellido_p = Column(String(255), nullable=False)
    apellido_m = Column(String(255), nullable=False)
    fecha_nacimiento = Column(DateTime, nullable=False)
    sexo = Column(String(255), nullable=False)
    numero_telefono = Column(String(255), nullable=False)
    correo_electronico = Column(String(255), nullable=False)
    expedientes = Column(BINARY(16), nullable=False)
    numero_seguro = Column(String(255), nullable=False)
    forma_pago = Column(String(255), nullable=False)
