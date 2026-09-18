from sqlalchemy import BigInteger, Column, DateTime, String, ForeignKey

from motor_de_conexion import Base


class Cita(Base):
    __tablename__ = "cita"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    fecha_hora_agendamiento = Column(DateTime, nullable=False)
    id_proceso = Column(BigInteger, ForeignKey('procesos.id'), nullable=False)
    id_tipo_cita = Column(BigInteger, ForeignKey('tipo_cita.id'), nullable=False)
    prioridad = Column(String(255), nullable=False)
    contacto = Column(String(255), nullable=False)
    id_cliente = Column(BigInteger, ForeignKey('clientes.id'), nullable=False)