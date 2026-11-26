from sqlalchemy import BigInteger, Column, Date, String, Text, ForeignKey

from database import Base


class CuidadosPasiente(Base):
    __tablename__ = "cuidados_pasiente"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    id_cliente = Column(BigInteger, ForeignKey('clientes.id'), nullable=False)
    fecha = Column(Date, nullable=False)
    detalle = Column(Text, nullable=False)
