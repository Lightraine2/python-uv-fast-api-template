from fastapi import FastAPI
from app.routers import auth, users

app = FastAPI(
    title="FastAPI Application",
    description="Base FastAPI application with PyJWT Authentication and some custom logging classes",
    version="1.0.0"
)

'''
Authenticated routes
'''

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
async def root():
    """
    Base API URL endpoint - no authentication required.
    """
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
    return {"status": "healthy"}

