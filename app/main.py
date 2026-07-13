from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="DevPilot Core API",
    version="0.1.0",
    description="Backend for the DevPilot developer productivity platform.",
)

# Include all routes defined in your single router file
app.include_router(api_router)