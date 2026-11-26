from sqlalchemy import BigInteger, Column, Text, String, ForeignKey

from database import Base


class Diagnostico(Base):
    __tablename__ = "diagnostico"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    id_cliente = Column(BigInteger, ForeignKey('clientes.id'), nullable=False)
    detalle_diagnostico = Column(Text, nullable=False)
