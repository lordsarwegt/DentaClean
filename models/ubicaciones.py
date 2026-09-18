from sqlalchemy import BigInteger, Column, String

from motor_de_conexion import Base


class Ubicaciones(Base):
    __tablename__ = "ubicaciones"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
