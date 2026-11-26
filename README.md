# DentaClean

## Arquitectura y cambios

El proyecto separa las responsabilidades del backend para que las rutas HTTP, la validación de datos y el acceso a la base de datos no estén concentrados en un solo archivo:

```text
main.py                 Punto de entrada ASGI y configuración de FastAPI
routes/                 Endpoints HTTP y dependencias de cada ruta
schemas/                Contratos de entrada y salida, definidos con Pydantic
crud/                   Operaciones de lectura y escritura con SQLAlchemy
models/                 Modelos ORM y tablas de la base de datos
database.py             Conexión, sesiones y dependencia get_db
alembic/                Configuración y revisiones de migración
frontend/
  *.html                Vistas de inicio de sesión, citas y pacientes
  js/                   JavaScript separado por vista
  styles.css            Estilos del frontend
  tailwind.config.js    Configuración compartida de Tailwind
```

`main.py` es el punto de entrada y orquestador de la aplicación: crea una instancia de `FastAPI`, configura CORS y registra los routers. No concentra toda la lógica del backend; por ejemplo, el router de usuarios se declara en `routes/usuarios.py`, valida los datos mediante `schemas/usuarios.py` y delega las operaciones de persistencia a `crud/usuarios.py`. Las sesiones de SQLAlchemy se proporcionan mediante `get_db` en `database.py`.

### Flujo de usuarios y contraseñas

El CRUD de usuarios utiliza SQLAlchemy. Al crear un usuario, `crud/usuarios.py` genera un hash con `bcrypt.hashpw` y una sal aleatoria (`bcrypt.gensalt`) antes de guardarlo. En el inicio de sesión, compara la contraseña recibida con el hash almacenado mediante `bcrypt.checkpw`.

> bcrypt realiza hashing unidireccional, no cifrado reversible: la contraseña original no se debe recuperar ni guardar en texto plano. La creación y el inicio de sesión usan bcrypt. Antes de usar operaciones de actualización de contraseña, hay que aplicar el mismo hashing: el helper `update_user` aún asigna el valor recibido directamente. Además, los esquemas de respuesta de `GET /usuarios` y `POST /usuarios` incluyen el campo `contraseña`; antes de producción, deben sustituirse por esquemas de salida que no expongan ni la contraseña ni su hash (como `UserOut`).

### Tecnologías

- **Python 3.11** y **FastAPI** para la API web, servida con **Uvicorn**.
- **Pydantic** para validar y definir los esquemas de entrada y salida.
- **SQLAlchemy** para el ORM y las sesiones de base de datos.
- **Microsoft SQL Server 2022**, conectado mediante **pyodbc** y Microsoft ODBC Driver 18.
- **Alembic** para versionar y aplicar cambios al esquema de la base de datos.
- **bcrypt** para el hashing y la verificación de contraseñas.
- **python-dotenv** para cargar configuración local desde `.env`.
- **Docker** y **Docker Compose** para ejecutar la API y SQL Server.
- En el navegador: **HTML**, **CSS** y **JavaScript**; las vistas usan **Tailwind CSS** desde CDN, fuentes de Google Fonts e iconos Material Symbols.

### Frontend y estructura de JavaScript

Las vistas HTML viven en `frontend/`, y cada vista carga su lógica desde un archivo independiente para mantener la presentación separada del comportamiento:

| Vista | Script |
|---|---|
| `frontend/log.html` | `frontend/js/log.js` |
| `frontend/citas.html` | `frontend/js/citas.js` |
| `frontend/pacientes.html` | `frontend/js/pacientes.js` |

`frontend/tailwind.config.js` contiene la configuración de Tailwind compartida por las vistas. `frontend/styles.css` y `frontend/app.js` pertenecen también al frontend.

Para iniciar los servicios con Docker Compose:

```powershell
docker compose up --build
```

El servicio de la API se publica en `http://localhost:8000` y SQL Server en el puerto `1433`. Compose monta el proyecto en el contenedor para reflejar los cambios locales durante el desarrollo. Los endpoints disponibles se documentan automáticamente en `http://localhost:8000/docs`.

## Migraciones con Alembic

Las migraciones se ejecutan desde la carpeta raíz del proyecto, donde se encuentran `alembic.ini`, `database.py` y la carpeta `alembic/`.

### 1. Preparar el entorno

Abre PowerShell en el proyecto:

```powershell
cd C:\Users\Usuario\Documents\GitHub\DentaClean
```

Si todavía no existe el entorno virtual, créalo:

```powershell
python -m venv .venv
```

Actívalo:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias necesarias:

```powershell
python -m pip install alembic sqlalchemy python-dotenv pyodbc
```

> Si PowerShell bloquea la activación del entorno, puedes ejecutar los comandos usando directamente `.venv\Scripts\python.exe`.

### 2. Configurar la conexión

`database.py` carga las siguientes variables desde un archivo `.env` en la raíz del proyecto:

```dotenv
servidor=nombre_o_ip_del_servidor
base_datos=nombre_de_la_base_de_datos
usuario=usuario_de_sql_server
password=contraseña_del_usuario
driver=ODBC Driver 18 for SQL Server
trust_server_certificate=no
```

Si la aplicación se ejecuta con Docker Compose, usa `servidor=db,1433`: `db` es el nombre del servicio y `1433` es el puerto interno de SQL Server. Si ejecutas la aplicación directamente en Windows, usa `servidor=localhost,1433`.

Docker Compose también usa el valor `password` de `.env` para inicializar el usuario `sa`, de modo que coincida con la contraseña que usa la aplicación. SQL Server conserva sus credenciales en el volumen `sqlserver_data`; cambiar `.env` no cambia la contraseña de un volumen ya inicializado. Para ese volumen, conserva la contraseña existente o cámbiala en SQL Server antes de actualizar `password` en `.env`. No elimines el volumen para resolver un error de inicio de sesión, porque contiene los datos de la base de datos.

No subas el archivo `.env` al repositorio porque contiene credenciales.

También debes tener instalado en Windows el controlador ODBC de SQL Server indicado en `driver`.

Si SQL Server usa un certificado autofirmado o emitido por una entidad no confiable (común en desarrollo), puedes establecer `trust_server_certificate=yes` para omitir la validación del certificado. Usa esta opción solo en desarrollo/local; en producción, instala un certificado confiable para el cliente y mantén el valor en `no`.

### 3. Comprobar la migración actual

Usando el entorno virtual activado:

```powershell
python -m alembic current
```

Para evitar confusiones entre el Python global y el entorno virtual, también puedes ejecutar siempre:

```powershell
.\.venv\Scripts\python.exe -m alembic current
```

El comando `alembic current` puede fallar si PowerShell encuentra una instalación global que no tiene `python-dotenv`. En ese caso, usa `python -m alembic` o la ruta explícita del entorno virtual.

### 4. Ver las migraciones disponibles

```powershell
python -m alembic history
```

Para ver la revisión más reciente:

```powershell
python -m alembic heads
```

### 5. Crear una migración

Después de modificar los modelos en `models/`, genera una migración automáticamente:

```powershell
python -m alembic revision --autogenerate -m "descripcion del cambio"
```

El archivo se creará en `alembic/versions/`.

Revisa siempre el archivo generado antes de aplicarlo. La generación automática no detecta todos los cambios y puede requerir ajustes manuales.

Para crear una migración vacía:

```powershell
python -m alembic revision -m "descripcion del cambio"
```

### 6. Aplicar migraciones

Aplicar todas las migraciones pendientes:

```powershell
python -m alembic upgrade head
```

Aplicar solo la siguiente migración:

```powershell
python -m alembic upgrade +1
```

### 7. Revertir migraciones

Revertir la última migración:

```powershell
python -m alembic downgrade -1
```

Volver a una revisión específica:

```powershell
python -m alembic downgrade ID_DE_REVISION
```

Revertir todas las migraciones:

```powershell
python -m alembic downgrade base
```

Ver la revisión actual antes y después de un cambio:

```powershell
python -m alembic current
```

### Flujo recomendado

```powershell
cd C:\Users\Usuario\Documents\GitHub\DentaClean
.\.venv\Scripts\Activate.ps1
python -m alembic current
python -m alembic revision --autogenerate -m "agregar cambio"
python -m alembic upgrade head
python -m alembic current
```

### Problemas frecuentes

**`ModuleNotFoundError: No module named 'dotenv'`**

El comando está usando otro Python. Instala las dependencias en el entorno correcto o usa la ruta explícita:

```powershell
.\.venv\Scripts\python.exe -m pip install alembic sqlalchemy python-dotenv pyodbc
.\.venv\Scripts\python.exe -m alembic current
```

**`alembic` no se reconoce o aparece un alias incorrecto**

Usa `python -m alembic` en lugar de `alembic`. Si existe un alias o función antigua en PowerShell, revisa el perfil:

```powershell
$PROFILE.CurrentUserCurrentHost
```

Elimina las definiciones antiguas de `alembic` del perfil y abre una nueva terminal.

**Error de conexión con SQL Server**

Comprueba que:

- El archivo `.env` está en la raíz del proyecto.
- Los nombres de las variables coinciden exactamente.
- SQL Server está disponible.
- El controlador ODBC está instalado.
- El usuario tiene permisos sobre la base de datos.

**Error al importar un modelo**

Revisa los imports en `models/` y confirma que el modelo está importado desde `models/__init__.py`. `alembic/env.py` importa `Base` y necesita conocer todos los modelos para que `--autogenerate` compare correctamente el esquema.
