from fastapi import FastAPI

app = FastAPI(
    title="DevPilot Core API",
    version="0.1.0",
    description="Backend for the DevPilot developer productivity platform.",
)


@app.get("/", tags=["Health"])
def health_check():
    return {
        "message": "Welcome to DevPilot Core"
    }