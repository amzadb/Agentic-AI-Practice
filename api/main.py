"""AI Agents API - Integrated FastAPI service combining multiple AI-powered APIs.

This is the main entry point for running all AI agent services in a unified application.
It integrates multiple specialized APIs into a single FastAPI instance running on port 8000.

Integrated APIs:
    1. SearchAgentsAPI - AI-powered search using various agents and search tools
    2. LearningAgentAPI - Personalized learning plan generation based on skills and goals

Architecture:
    This application uses FastAPI's router pattern to create a modular, scalable
    microservices architecture. Each API is implemented as a separate router that can be:
    - Run independently as a standalone microservice (on its own port)
    - Integrated into this main app for unified deployment
    - Easily enabled/disabled by commenting out router includes

Endpoints:
    GET  / - Root endpoint with API information
    POST /search - Execute AI-powered search queries (SearchAgentsAPI)
    POST /learning-plan - Generate personalized learning plans (LearningAgentAPI)

Usage:
    Development mode with auto-reload:
        $ python -m api.main
        or
        $ uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
    
    Production deployment:
        $ uvicorn api.main:app --host 0.0.0.0 --port 8000 --workers 4

API Documentation:
    Interactive docs available at:
    - Swagger UI: http://localhost:8000/docs

Configuration:
    - Port: 8000 (configurable)
    - CORS: Enabled for all origins (development mode)
    - API Keys: Loaded from .env file via each router

Author: Amzad Basha
Version: 1.0.0
"""

from fastapi import FastAPI

from api.SearchAgentsAPI import router as search_router
from api.LearningAgentAPI import router as learning_router
from util.cors_config import setup_cors

# Initialize the main FastAPI application
app = FastAPI(
    title="AI Agents API",
    version="1.0.0",
    description="Unified API gateway for AI-powered search and learning services"
)

# Setup CORS middleware using utility function
setup_cors(app)

# Include API routers
# Each router provides a complete set of endpoints from its respective API
# Routers can be easily enabled/disabled by commenting out the include statement

# Search Agents API Router
# Provides: POST /search
app.include_router(search_router, prefix="", tags=["search"])

# Learning Agent API Router
# Provides: POST /learning-plan
app.include_router(learning_router, prefix="", tags=["learning"])


@app.get("/")
def root():
    """Root endpoint providing API information and available endpoints.
    
    Returns a welcome message and a list of all available API endpoints
    in the integrated application.
    
    Returns:
        dict: API information including:
            - message: Welcome message
            - endpoints: Dictionary of available endpoint paths
            - docs: Link to interactive documentation
    
    Example:
        GET /
        
        Response:
            {
                "message": "AI Agents API",
                "endpoints": {
                    "search": "/search",
                    "learning_plan": "/learning-plan"
                },
                "documentation": {
                    "swagger": "/docs",
                    "redoc": "/redoc"
                }
            }
    """
    return {
        "message": "AI Agents API",
        "version": "1.0.0",
        "endpoints": {
            "search": "/search",
            "learning_plan": "/learning-plan"
        },
        "documentation": "/docs"
    }


if __name__ == "__main__":
    """Entry point for running the integrated API application.
    
    Starts all integrated APIs on a single port (8000) with the following configuration:
    - Host: 0.0.0.0 (accessible from all network interfaces)
    - Port: 8000
    - Hot reload: Disabled (use uvicorn --reload for development)
    
    For development with auto-reload, use:
        uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
    
    Access points:
        - API: http://localhost:8000
        - Swagger Docs: http://localhost:8000/docs
    """
    import uvicorn
    
    print("=" * 60)
    print("Starting AI Agents API (Integrated Mode)")
    print("=" * 60)
    print("Server: http://localhost:8000")
    print("Swagger Documentation: http://localhost:8000/docs")
    print()
    print("Available Endpoints:")
    print("  - POST /search - AI-powered search")
    print("  - POST /learning-plan - Personalized learning plans")
    print("=" * 60)
    
    uvicorn.run(app, host="localhost", port=8000)