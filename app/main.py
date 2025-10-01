from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Application",
    description="Base FastAPI application with PyJWT Authentication and some custom logging classes",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Public endpoint - no authentication required."""
    return {
        "message": "Welcome to FastAPI with JWT Authentication",
        "docs": "/docs",
        "endpoints": {
            "login": "POST /auth/token",
            "me": "GET /users/me (protected)",
            "items": "GET /users/me/items (protected)",
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}