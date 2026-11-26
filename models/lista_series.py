from sqlalchemy import BigInteger, Column, Date, String, ForeignKey

from database import Base


class ListaSeries(Base):
    __tablename__ = "lista_series"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    fecha_vencimiento = Column(Date, nullable=False)
    id_producto = Column(BigInteger, ForeignKey('lista_productos.id'), nullable=False)
