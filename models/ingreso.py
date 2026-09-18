from sqlalchemy import BigInteger, Column, Date, String, ForeignKey

from motor_de_conexion import Base


class Ingreso(Base):
    __tablename__ = "ingreso"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    id_orden_compra = Column(BigInteger, ForeignKey('orden_compra.id'), nullable=False)
    fecha_ingreso = Column(Date, nullable=False)
    id_usuario = Column(BigInteger, ForeignKey('usuarios.id'), nullable=False)
