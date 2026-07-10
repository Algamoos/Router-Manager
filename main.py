from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from routers import auth, dashboard, interfaces, ip_address, hotspot


app = FastAPI(
    title="MikroTik Manager",
    version="1.0.0"
)


# Session
app.add_middleware(
    SessionMiddleware,
    secret_key="change-this-secret-key"
)


# Static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(interfaces.router)
app.include_router(ip_address.router)
app.include_router(hotspot.router)