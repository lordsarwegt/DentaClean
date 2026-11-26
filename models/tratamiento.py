from sqlalchemy import BigInteger, Column, String, ForeignKey

from database import Base


class Tratamiento(Base):
    __tablename__ = "tratamiento"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    id_proceso = Column(BigInteger, ForeignKey('procesos.id'), nullable=False)
    descripcion = Column(String(255), nullable=False)
    id_diagnotico = Column(BigInteger, ForeignKey('diagnostico.id'), nullable=False)
