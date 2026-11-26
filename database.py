import os
import urllib

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

servidor = os.getenv("servidor")
base_datos = os.getenv("base_datos")
usuario = os.getenv("usuario")
password = os.getenv("password")
driver = os.getenv("driver")
trust_server_certificate = os.getenv("trust_server_certificate", "no")

params = urllib.parse.quote_plus(
    f"TrustServerCertificate={trust_server_certificate};"
    f"DRIVER={driver};SERVER={servidor};DATABASE={base_datos};"
    f"UID={usuario};PWD={password}"
)
DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def create_database_if_not_exists():
    """Crea la base de datos en SQL Server si aún no existe."""
    if not all([servidor, base_datos, usuario, password, driver]):
        raise ValueError(
            "Faltan variables de entorno: servidor, base_datos, usuario, password o driver"
        )

    server_params = urllib.parse.quote_plus(
        f"TrustServerCertificate={trust_server_certificate};"
        f"DRIVER={driver};SERVER={servidor};UID={usuario};PWD={password}"
    )
    server_url = f"mssql+pyodbc:///?odbc_connect={server_params}"

    server_engine = create_engine(server_url, pool_pre_ping=True)

    with server_engine.connect() as conn:
        db_exists = conn.execute(
            text("SELECT 1 FROM sys.databases WHERE name = :db_name"),
            {"db_name": base_datos},
        ).fetchone()

        if not db_exists:
            conn.execute(text(f"CREATE DATABASE [{base_datos}]"))
            conn.commit()

    server_engine.dispose()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    create_database_if_not_exists()
    print(f"Base de datos '{base_datos}' verificada/creada correctamente.")
