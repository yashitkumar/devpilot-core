# routes.py
from fastapi import APIRouter
from app.api.routes import health
from app.modules.users import router as users_router

# 1. Create the central master router
api_router = APIRouter()

# 2. Include the health route in the central router
api_router.include_router(health.router, prefix="/api", tags=["Health"])

api_router.include_router(users_router.router, prefix="/api", tags=["Users"])
