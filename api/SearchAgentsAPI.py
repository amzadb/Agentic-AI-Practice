"""SearchAgentsAPI - FastAPI service for AI-powered search operations.

This module provides a FastAPI-based REST API for executing search queries using
various AI agents (e.g., Perplexity, Groq, DeepSeek) and search tools (e.g., DuckDuckGo).

The API can run in two modes:
1. As a standalone microservice on port 8001
2. As a router integrated into a larger FastAPI application

Endpoints:
    POST /search - Execute a search query with specified agent and search tool

Examples:
    Standalone mode:
        $ python -m api.SearchAgentsAPI
    
    Integration mode:
        from api.SearchAgentsAPI import router
        app.include_router(router)

Author: Amzad Basha
Version: 1.0.0
"""

from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from agents.MySearchAgent import MySearchAgent

from dotenv import load_dotenv
load_dotenv()  # Load API keys from .env file

# Router instance for integration with other FastAPI applications
router = APIRouter()

class SearchRequest(BaseModel):
    """Request model for search endpoint.
    
    Attributes:
        agent (str): The AI agent to use for search.
            Options: 'Open AI', 'Gemini', 'Anthropic', 'Groq'
        search_tool (str): The search tool/engine to use.
            Options: 'Duck Duck Go', 'Google Search', etc.
        prompt (str): The search query or prompt to execute.
    
    Example:
        {
            "agent": "Open AI",
            "search_tool": "Duck Duck Go",
            "prompt": "What is generative AI?"
        }
    """
    agent: str
    search_tool: str
    prompt: str

@router.post("/search")
def search(request: SearchRequest):
    """Execute a search query using specified AI agent and search tool.
    
    This endpoint processes search requests by initializing the appropriate AI agent
    with the specified search tool, executing the query, and returning the results.
    
    Args:
        request (SearchRequest): The search request containing agent type,
            search tool, and the search prompt.
    
    Returns:
        dict: A dictionary containing:
            - prompt (str): The original search query
            - result (str): The search result content from the AI agent
    
    Raises:
        HTTPException: 400 error if the agent/search tool is invalid or
            if the search execution fails.
    
    Example:
        Request:
            POST /search
            {
                "agent": "Groq",
                "search_tool": "Duck Duck Go",
                "prompt": "What is generative AI?"
            }
        
        Response:
            {
                "prompt": "What is generative AI?",
                "result": "Generative AI is a type of artificial intelligence..."
            }
    """
    try:
        # Initialize the search agent with specified agent type and search tool
        agent = MySearchAgent(request.agent, request.search_tool)
        
        # Execute the search query
        result = agent.run(request.prompt)
        
        # Extract content from result object (handles different response types)
        content = getattr(result, "content", str(result))
        
        return {
            "prompt": request.prompt,
            "result": content
        }
    except Exception as e:
        # Return detailed error message for debugging
        raise HTTPException(status_code=400, detail=str(e))

# Standalone FastAPI app (for running SearchAgentsAPI independently)
def create_app():
    """Create and configure a standalone FastAPI application.
    
    Creates a complete FastAPI application instance with CORS middleware,
    search routing, and a root endpoint. This function is used when running
    SearchAgentsAPI as an independent microservice.
    
    Returns:
        FastAPI: A configured FastAPI application instance with:
            - Title: "Search Agents API"
            - Version: "1.0.0"
            - CORS enabled for all origins (development mode)
            - Search router included
            - Root endpoint at "/"
    
    Example:
        app = create_app()
        uvicorn.run(app, host="localhost", port=8001)
    
    Note:
        CORS is configured with allow_origins=["*"] for development.
        For production, restrict origins to specific domains.
    """
    app = FastAPI(
        title="Search Agents API",
        version="1.0.0",
        description="AI-powered search API supporting multiple agents and search tools"
    )
    
    # Enable CORS for cross-origin requests (configured for development)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # TODO: Restrict origins in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include the search router
    app.include_router(router)
    
    @app.get("/")
    def root():
        """Root endpoint providing API information.
        
        Returns:
            dict: API name and available endpoints.
        """
        return {
            "message": "Search Agents API",
            "endpoint": "/search",
            "docs": "/docs"
        }
    
    return app

# Run independently if this file is executed directly
if __name__ == "__main__":
    """Entry point for standalone execution.
    
    Starts the SearchAgentsAPI as an independent microservice on port 8001.
    Access the API at: http://localhost:8001
    API documentation: http://localhost:8001/docs
    
    Usage:
        python -m api.SearchAgentsAPI
    """
    app = create_app()
    print("Starting Search Agents API on http://localhost:8001")
    print("API Documentation available at http://localhost:8001/docs")
    uvicorn.run(app, host="localhost", port=8001)