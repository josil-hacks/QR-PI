from fastapi import FastAPI

from qr_pi.api.routes import router

app = FastAPI(
    title="QR Generator API",
    version="0.1.0",
)

app.include_router(router)