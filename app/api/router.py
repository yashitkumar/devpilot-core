# routes.py
from fastapi import APIRouter
from app.api.routes import health

# 1. Create the central master router
api_router = APIRouter()

# 2. Include the health route in the central router
api_router.include_router(health.router, prefix="/api", tags=["Health"])
