"""Main FastAPI Application"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1 import routes

# Initialize FastAPI app
app = FastAPI(
    title="FastAPI Application",
    description="A modern Python web application using FastAPI",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(routes.router, prefix="/api/v1", tags=["v1"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Application"}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
