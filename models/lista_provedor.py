from sqlalchemy import BigInteger, Column, String

from motor_de_conexion import Base


class ListaProvedor(Base):
    __tablename__ = "lista_provedor"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(String(255), nullable=False)
    correo_electronico = Column(String(255), nullable=False)
    numero_telefono = Column(String(255), nullable=False)
