from sqlalchemy import BigInteger, Column, String

from database import Base


class Procesos(Base):
    __tablename__ = "procesos"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(String(255), nullable=False)
