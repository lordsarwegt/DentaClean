from sqlalchemy import BigInteger, Column, DateTime, String, ForeignKey
from sqlalchemy.sql.sqltypes import Numeric

from database import Base


class Factura(Base):
    __tablename__ = "factura"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    razon_social = Column(String(255), nullable=False)
    rfc = Column(String(255), nullable=False)
    regimen_fiscal = Column(String(255), nullable=False)
    codigo_posta = Column(String(255), nullable=False)
    id_cliente = Column(BigInteger, ForeignKey('clientes.id'), nullable=False)
    rfc_cliente = Column(String(255), nullable=False)
    codig_posta_cliente = Column(String(255), nullable=False)
    cfdi = Column(String(255), nullable=False)
    fecha_hora_emision = Column(DateTime, nullable=False)
    id_proceso = Column(BigInteger, ForeignKey('procesos.id'), nullable=False)
    impuesto = Column(Numeric(precision=8, scale=2), nullable=False)
    forma_pago = Column(String(255), nullable=False)
    metodo_pago = Column(BigInteger, nullable=False)
