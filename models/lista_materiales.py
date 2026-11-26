from sqlalchemy import BigInteger, Column, Integer, String, ForeignKey

from database import Base


class ListaMateriales(Base):
    __tablename__ = "lista_materiales"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_producto = Column(BigInteger, ForeignKey('lista_productos.id', name='lista_materiales_id_producto_foreign'), nullable=False)
    id_serie = Column(BigInteger, ForeignKey('lista_series.id', name='lista_materiales_id_serie_foreign'), nullable=False)
    id_cita = Column(BigInteger, ForeignKey('cita.id', name='lista_materiales_id_cita_foreign'), nullable=False)
    descripcion = Column(String(255), nullable=False)
    cantidad = Column(Integer, nullable=False)
    estatus = Column(String(255), nullable=False)
