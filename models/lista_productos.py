from sqlalchemy import BigInteger, Boolean, Column, String, Text
from sqlalchemy.sql.sqltypes import Numeric

from database import Base


class ListaProductos(Base):
    __tablename__ = "lista_productos"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=False)
    marca = Column(String(255), nullable=False)
    costo = Column(Numeric(precision=8, scale=2), nullable=False)
    registro_sanitario = Column(String(255), nullable=False)
    cadena_frio = Column(Boolean, nullable=False)
