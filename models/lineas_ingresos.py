from sqlalchemy import BigInteger, Column, String, ForeignKey

from database import Base


class LineasIngresos(Base):
    __tablename__ = "lineas_ingresos"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_ingreso = Column(BigInteger, ForeignKey('ingreso.id', name='lineas_ingresos_id_ingreso_foreign'), nullable=False)
    id_serie = Column(BigInteger, ForeignKey('lista_series.id', name='lineas_ingresos_id_serie_foreign'), nullable=False)
    id_producto = Column(BigInteger, ForeignKey('lista_productos.id', name='lineas_ingresos_id_producto_foreign'), nullable=False)
    id_cita = Column(BigInteger, ForeignKey('cita.id', name='lineas_ingresos_id_cita_foreign'), nullable=False)
    status_validacion = Column(String(255), nullable=False)
