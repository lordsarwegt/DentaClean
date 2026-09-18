from sqlalchemy import BigInteger, Column, String

from motor_de_conexion import Base


class TipoCita(Base):
    __tablename__ = "tipo_cita"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    tipo = Column(String(255), nullable=False)
