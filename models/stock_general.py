from sqlalchemy import BigInteger, Column, DateTime, Integer, ForeignKey

from database import Base


class StockGeneral(Base):
    __tablename__ = "stock_general"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_serie = Column(BigInteger, ForeignKey('lista_series.id', name='stock_general_id_serie_foreign'), nullable=False)
    id_producto = Column(BigInteger, ForeignKey('lista_productos.id', name='stock_general_id_producto_foreign'), nullable=False)
    id_ubicaciones = Column(BigInteger, ForeignKey('ubicaciones.id', name='stock_general_id_ubicaciones_foreign'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    cantidad_reseravada = Column(Integer, nullable=False)
    fecha_ingreso = Column(DateTime, nullable=False)
    fecha_ultimo_movimiento = Column(DateTime, nullable=False)
    id_cita = Column(BigInteger, ForeignKey('cita.id', name='stock_general_id_cita_foreign'), nullable=False)

