from sqlalchemy import BigInteger, Column, String

from database import Base


class Ubicaciones(Base):
    __tablename__ = "ubicaciones"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
