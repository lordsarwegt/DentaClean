from sqlalchemy import BigInteger, Column, Date, String, ForeignKey
from sqlalchemy.sql.sqltypes import Numeric

from motor_de_conexion import Base


class Cotizacion(Base):
    __tablename__ = "cotizacion"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    id_proceso = Column(BigInteger, ForeignKey('procesos.id'), nullable=False)
    id_clinica = Column(BigInteger, ForeignKey('clinicas.id'), nullable=False)
    empresa = Column(String(255), nullable=False)
    direccion = Column(String(255), nullable=False)
    numero_telefono = Column(String(255), nullable=False)
    id_cliente = Column(BigInteger, ForeignKey('clientes.id'), nullable=False)
    fecha_emision = Column(Date, nullable=False)
    fecha_vigencia = Column(Date, nullable=False)
    sub_total = Column(Numeric(precision=8, scale=2), nullable=False)
    impuesto_aplicado = Column(Numeric(precision=8, scale=2), nullable=False)
    total = Column(Numeric(precision=8, scale=2), nullable=False)
    metodo_pago = Column(String(255), nullable=False)
    numero_seguro = Column(String(255), nullable=False)
