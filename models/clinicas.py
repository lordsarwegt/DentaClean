from sqlalchemy import BigInteger, Column, String

from database import Base


class Clinicas(Base):
    __tablename__ = "clinicas"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    direccion = Column(String(255), nullable=False)
    rfc = Column(String(255), nullable=False)
    cp = Column(String(255), nullable=False)
    gerente = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=False)
