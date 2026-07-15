from fastapi import FastAPI
from app.api.router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.description,
)

@app.get("/", tags=["Root"])
async def root():
    return {
        "environment": settings.environment,
        "status": "running",
        "service": settings.app_name,
        "version": settings.app_version
    }

# Include all routes defined in your single router file
app.include_router(api_router)