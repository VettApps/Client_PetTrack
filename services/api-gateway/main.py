from fastapi import FastAPI, Request
import httpx
import os

app = FastAPI()

AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-service:8000")
APPOINTMENTS_SERVICE_URL = os.getenv("APPOINTMENTS_SERVICE_URL", "http://appointments-service:8000")

@app.api_route("/auth/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_auth(request: Request, path: str):
    url = f"{AUTH_SERVICE_URL}/{path}"
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            url,
            headers=request.headers.raw,
            content=await request.body()
        )
    return response.json(), response.status_code

@app.api_route("/appointments/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_appointments(request: Request, path: str):
    url = f"{APPOINTMENTS_SERVICE_URL}/{path}"
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            url,
            headers=request.headers.raw,
            content=await request.body()
        )
    return response.json(), response.status_code