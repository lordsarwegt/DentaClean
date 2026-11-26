from sqlalchemy import BigInteger, Column, String, ForeignKey

from database import Base


class MovimientoMateriales(Base):
    __tablename__ = "movimiento_materiales"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    id_ubicacion_destino = Column(BigInteger, ForeignKey('ubicaciones.id', name='movimiento_materiales_id_ubicacion_destino_foreign'), nullable=False)
    id_ubicacion_origen = Column(BigInteger, ForeignKey('ubicaciones.id', name='movimiento_materiales_id_ubicacion_origen_foreign'), nullable=False)
    id_serie = Column(BigInteger, ForeignKey('lista_series.id', name='movimiento_materiales_id_serie_foreign'), nullable=False)
    id_producto = Column(BigInteger, ForeignKey('lista_productos.id', name='movimiento_materiales_id_producto_foreign'), nullable=False)
    id_cita = Column(BigInteger, ForeignKey('cita.id', name='movimiento_materiales_id_cita_foreign'), nullable=False)
