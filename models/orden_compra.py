from sqlalchemy import BigInteger, Column, Date, DateTime, String, ForeignKey

from database import Base


class OrdenCompra(Base):
    __tablename__ = "orden_compra"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    estatus = Column(String(255), nullable=False)
    id_usuario = Column(BigInteger, ForeignKey('usuarios.id'), nullable=False)
    fecha_solicitud = Column(Date, nullable=False)
    fecha_ultima_actualizacion = Column(DateTime, nullable=False)
