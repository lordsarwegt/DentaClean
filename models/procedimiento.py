from sqlalchemy import BigInteger, Column, Integer, String
from sqlalchemy.sql.sqltypes import Numeric

from motor_de_conexion import Base


class Procedimiento(Base):
    __tablename__ = "procedimiento"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    codigo_servicio = Column(String(255), nullable=False)
    cantidad = Column(Integer, nullable=False)
    descripcion = Column(String(255), nullable=False)
    precio_unitario = Column(Numeric(precision=8, scale=2), nullable=False)
