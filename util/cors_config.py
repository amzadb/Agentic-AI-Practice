"""CORS Configuration Utility for FastAPI Applications.

This module provides centralized CORS (Cross-Origin Resource Sharing) configuration
for all FastAPI applications in the AI Agents project. It ensures consistent CORS
setup across multiple services (SearchAgentsAPI, LearningAgentAPI, and main.py).

CORS Settings:
    - allow_origins: ["*"] - Allow requests from all origins (development mode)
    - allow_credentials: True - Allow cookies and authentication headers
    - allow_methods: ["*"] - Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    - allow_headers: ["*"] - Allow all headers in requests

Warning:
    For production environments, restrict allow_origins to specific domains instead
    of using ["*"] to enhance security.

Example:
    from fastapi import FastAPI
    from util.cors_config import setup_cors
    
    app = FastAPI()
    setup_cors(app)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def setup_cors(app: FastAPI) -> None:
    """Configure CORS middleware for a FastAPI application.
    
    This function sets up CORS (Cross-Origin Resource Sharing) middleware on a FastAPI
    application instance. It enables cross-origin requests with permissive defaults
    suitable for development environments.
    
    Args:
        app (FastAPI): The FastAPI application instance to configure.
    
    Returns:
        None: Modifies the app instance in-place.
    
    Configuration Details:
        - allow_origins: ["*"] - Allows requests from any origin
        - allow_credentials: True - Allows authentication credentials
        - allow_methods: ["*"] - Allows all HTTP methods
        - allow_headers: ["*"] - Allows all headers
    
    Example:
        >>> from fastapi import FastAPI
        >>> from util.cors_config import setup_cors
        >>> 
        >>> app = FastAPI()
        >>> setup_cors(app)
        >>> # CORS is now configured on the app
    
    Note:
        SECURITY WARNING: The current configuration with allow_origins=["*"] and
        allow_credentials=True is suitable only for development. For production,
        restrict allow_origins to your specific domain(s):
        
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["https://your-domain.com"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    """
    # Enable CORS for cross-origin requests
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allow all origins in development
        allow_credentials=True,  # Allow authentication credentials
        allow_methods=["*"],  # Allow all HTTP methods
        allow_headers=["*"],  # Allow all headers
    )
