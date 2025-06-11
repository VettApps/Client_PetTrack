from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os

app = FastAPI()

# CORS: Permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["http://localhost:8080"] si quieres restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# URLs internas de los microservicios
AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-service:8000")
APPOINTMENTS_SERVICE_URL = os.getenv("APPOINTMENTS_SERVICE_URL", "http://appointments-service:8000")


# --- AUTH SERVICE PROXIES ---

@app.post("/auth/register")
async def register(request: Request):
    body = await request.body()
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{AUTH_SERVICE_URL}/register", content=body, headers=request.headers)
    return JSONResponse(status_code=response.status_code, content=response.json())

@app.post("/auth/login")
async def login(request: Request):
    body = await request.body()
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{AUTH_SERVICE_URL}/login", content=body, headers=request.headers)
    return JSONResponse(status_code=response.status_code, content=response.json())

@app.get("/auth/users")
async def get_users():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://auth-service:8000/users")
    return Response(content=response.content, status_code=response.status_code)
    
# --- APPOINTMENTS SERVICE PROXIES (Ejemplo) ---

@app.get("/appointments/")
async def get_appointments():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{APPOINTMENTS_SERVICE_URL}/appointments/")
    return JSONResponse(status_code=response.status_code, content=response.json())
