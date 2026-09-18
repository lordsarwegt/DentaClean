from sqlalchemy import BigInteger, Column, Date, String, Text, ForeignKey

from motor_de_conexion import Base


class OrdenRadiografia(Base):
    __tablename__ = "orden_radiografia"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    id_cliente = Column(BigInteger, ForeignKey('clientes.id'), nullable=False)
    informacion_cliente = Column(Text, nullable=False)
    tipo_radiografia = Column(String(255), nullable=False)
    vigencia_solicitud = Column(Date, nullable=False)
