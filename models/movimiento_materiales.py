from sqlalchemy import BigInteger, Column, String, ForeignKey

from motor_de_conexion import Base


class MovimientoMateriales(Base):
    __tablename__ = "movimiento_materiales"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    id_ubicacion_destino = Column(BigInteger, ForeignKey('ubicaciones.id'), nullable=False)
    id_ubicacion_origen = Column(BigInteger, ForeignKey('ubicaciones.id'), nullable=False)
    id_serie = Column(BigInteger, ForeignKey('lista_series.id'), nullable=False)
    id_producto = Column(BigInteger, ForeignKey('lista_productos.id'), nullable=False)
    id_cita = Column(BigInteger, ForeignKey('cita.id'), nullable=False)
