import sys
from os.path import abspath, dirname

# 1. Asegura que Alembic encuentre tus archivos en la raíz del proyecto
sys.path.insert(0, dirname(dirname(abspath(__file__))))

# 2. Importa la Base y tus modelos
# (Si la creaste en motor_de_conexion, impórtala de ahí)
from database import DATABASE_URL

# 3. Es MUY IMPORTANTE importar también tus modelos aquí abajo
# Aunque no los uses directamente, esto hace que Alembic se entere de que existen
from models import Base  # noqa: F403, F401   

from logging.config import fileConfig

from sqlalchemy import engine_from_config

from sqlalchemy import pool

from alembic import context


config = context.config

# Interpreta el archivo de configuración para el logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Define los metadatos de tus modelos para el --autogenerate
target_metadata = Base.metadata

# Reutiliza exactamente la configuración de conexión de la aplicación.
config.set_main_option("sqlalchemy.url", DATABASE_URL.replace("%", "%%"))


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
