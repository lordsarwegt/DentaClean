from sqlalchemy import BigInteger, Column, String, ForeignKey

from motor_de_conexion import Base


class LineasIngresos(Base):
    __tablename__ = "lineas_ingresos"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_ingreso = Column(BigInteger, ForeignKey('ingreso.id'), nullable=False)
    id_serie = Column(BigInteger, ForeignKey('lista_series.id'), nullable=False)
    id_producto = Column(BigInteger, ForeignKey('lista_productos.id'), nullable=False)
    id_cita = Column(BigInteger, ForeignKey('cita.id'), nullable=False)
    status_validacion = Column(String(255), nullable=False)
