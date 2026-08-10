from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.router import api_router
from app.core.config import settings
from app.modules.auth.exceptions import InvalidCredentialsError, InvalidTokenError
from app.modules.users.exceptions import UserAlreadyExistsError

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

@app.exception_handler(UserAlreadyExistsError)
async def user_already_exists_handler(request:Request, exc: UserAlreadyExistsError):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc)},
    )

@app.exception_handler(InvalidCredentialsError)
async def invalid_credentials_handler(request:Request, exc: InvalidCredentialsError):
    return JSONResponse(
        status_code=401,
        content={"detail": str(exc)},
    )

@app.exception_handler(InvalidTokenError)
async def invalid_token_handler(request:Request, exc: InvalidTokenError):
    return JSONResponse(
        status_code=401,
        content={"detail": str(exc)},
    )

# Include all routes defined in your single router file
app.include_router(api_router)