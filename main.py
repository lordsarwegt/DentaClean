from fastapi import FastAPI
from routes import usuarios
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5500",
    "http://127.0.0.1:5500"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],                       # GET, POST, DELETE, etc.
    allow_headers=["*"],                       # Content-Type, etc.
)
#frontend_dir = Path(__file__).parent / "frontend"


@app.get("/api/saludo")
async def obtener_saludo():
    return {"mensaje": "Hola desde FastAPI!"}

app.include_router(usuarios.router, prefix="/usuarios", tags=["usuarios"])