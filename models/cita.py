from sqlalchemy import BigInteger, Column, DateTime, String, ForeignKey

from database import Base


class Cita(Base):
    __tablename__ = "cita"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    fecha_hora_agendamiento = Column(DateTime, nullable=False)
    id_proceso = Column(BigInteger, ForeignKey('procesos.id', name='cita_id_proceso_foreign'), nullable=False)
    id_tipo_cita = Column(BigInteger, ForeignKey('tipo_cita.id', name='cita_id_tipo_cita_foreign'), nullable=False)
    prioridad = Column(String(255), nullable=False)
    contacto = Column(String(255), nullable=False)
    id_cliente = Column(BigInteger, ForeignKey('clientes.id', name='cita_id_cliente_foreign'), nullable=False)