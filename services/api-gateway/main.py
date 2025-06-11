from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx
import os

app = FastAPI()

AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-service:8000")
APPOINTMENTS_SERVICE_URL = os.getenv("APPOINTMENTS_SERVICE_URL", "http://appointments-service:8000")

@app.api_route("/auth/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_auth(request: Request, path: str):
    url = f"{AUTH_SERVICE_URL}/{path}"
    headers = dict(request.headers)
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            url,
            headers=headers,
            content=await request.body()
        )
    try:
        content = response.json()
        return JSONResponse(content=content, status_code=response.status_code)
    except Exception:
        return Response(content=response.content, status_code=response.status_code, media_type=response.headers.get("content-type"))

@app.api_route("/appointments/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_appointments(request: Request, path: str = ""):
    full_path = f"/appointments/{path}" if path else "/appointments"
    url = f"{APPOINTMENTS_SERVICE_URL}{full_path}"
    print(f"Proxying request to: {url}")  # Debug

    headers = dict(request.headers)
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            url,
            headers=headers,
            content=await request.body()
        )
    try:
        content = response.json()
        return JSONResponse(content=content, status_code=response.status_code)
    except Exception:
        return Response(content=response.content, status_code=response.status_code, media_type=response.headers.get("content-type"))
