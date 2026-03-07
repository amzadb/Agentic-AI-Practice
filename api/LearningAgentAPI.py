"""LearningAgentAPI - FastAPI service for personalized learning plan generation.

This module provides a FastAPI-based REST API for generating personalized learning plans
using AI. The service analyzes user skills, weaknesses, and career aspirations to create
customized learning roadmaps with recommended resources from YouTube, Udemy, and other platforms.

The API can run in two modes:
1. As a standalone microservice on port 8002
2. As a router integrated into a larger FastAPI application

Endpoints:
    POST /learning-plan - Generate a personalized learning plan

Features:
    - Skill gap analysis
    - Personalized learning roadmaps
    - Resource recommendations (YouTube, Udemy, etc.)
    - LinkedIn profile review and optimization suggestions (optional)

Examples:
    Standalone mode:
        $ python -m api.LearningAgentAPI
    
    Integration mode:
        from api.LearningAgentAPI import router
        app.include_router(router)

Author: Your Name
Version: 1.0.0
"""

from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from agents.MyLearningAgent import MyLearningAgent

from dotenv import load_dotenv
load_dotenv()  # Load API keys from .env file

# Router instance for integration with other FastAPI applications
router = APIRouter()

class LearningPlanRequest(BaseModel):
    """Request model for learning plan generation endpoint.
    
    Attributes:
        strong_skills (str): Comma-separated list of user's strong/existing skills.
            Example: "Python, Machine Learning, Data Analysis"
        weak_areas (str): Areas where the user needs improvement or wants to learn.
            Example: "Web Development, DevOps, Cloud Computing"
        aspirations (str): Career goals and aspirations.
            Example: "Become an AI Engineer", "Transition to Full-Stack Development"
        linkedin_url (str, optional): LinkedIn profile URL for profile review and
            optimization suggestions. Defaults to None.
    
    Example:
        {
            "strong_skills": "Python, Machine Learning",
            "weak_areas": "Web Development, Cloud Computing",
            "aspirations": "Become a Full-Stack AI Engineer",
            "linkedin_url": "https://linkedin.com/in/yourprofile"
        }
    """
    strong_skills: str
    weak_areas: str
    aspirations: str
    linkedin_url: str = None

@router.post("/learning-plan")
def generate_learning_plan(request: LearningPlanRequest):
    """Generate a personalized learning plan based on user's skills and goals.
    
    This endpoint analyzes the user's current skills, areas for improvement, and career
    aspirations to create a customized learning roadmap. The plan includes recommended
    resources from platforms like YouTube, Udemy, and other educational sources.
    
    If a LinkedIn URL is provided, the service also reviews the profile and suggests
    improvements to make it more attractive for the user's career goals.
    
    Args:
        request (LearningPlanRequest): The learning plan request containing:
            - strong_skills: User's existing strengths
            - weak_areas: Areas needing improvement
            - aspirations: Career goals
            - linkedin_url (optional): LinkedIn profile for review
    
    Returns:
        dict: A dictionary containing:
            - learning_plan (str): A comprehensive, formatted learning plan with:
                * Step-by-step learning roadmap
                * Recommended YouTube videos with links
                * Suggested Udemy courses with links
                * Additional learning resources
                * LinkedIn profile improvement tips (if URL provided)
    
    Raises:
        HTTPException: 500 error if the learning plan generation fails or
            if there's an issue with the AI agent.
    
    Example:
        Request:
            POST /learning-plan
            {
                "strong_skills": "Python, Machine Learning",
                "weak_areas": "Web Development, DevOps",
                "aspirations": "Become a Full-Stack AI Engineer",
                "linkedin_url": "https://linkedin.com/in/yourprofile"
            }
        
        Response:
            {
                "learning_plan": "## Personalized Learning Plan\n\n### Phase 1: Web Development Fundamentals\n1. HTML & CSS Basics\n   - YouTube: [HTML Crash Course](...)\n   - Udemy: [Complete Web Developer Bootcamp](...)\n..."
            }
    """
    try:
        # Build the prompt with user's skills, weaknesses, and aspirations
        prompt = (
            f"My strong skills: {request.strong_skills}\n"
            f"My weak areas: {request.weak_areas}\n"
            f"My aspirations: {request.aspirations}\n"
        )
        
        # Add LinkedIn profile review request if URL is provided
        if request.linkedin_url:
            prompt += f"My LinkedIn profile: {request.linkedin_url}\n"
            prompt += (
                "Please review my LinkedIn profile and suggest improvements to make it more attractive for my aspirations. "
            )
        
        # Add instructions for learning plan generation
        prompt += (
            "Please create a personalized learning plan for me. "
            "Suggest relevant YouTube videos, Udemy courses, and other resources for my weak areas and aspirations. "
            "Format the output as a step-by-step plan with links."
        )

        # Initialize the learning agent and generate the plan
        agent = MyLearningAgent()
        result = agent.run(prompt)
        
        # Extract content from result object (handles different response types)
        content = result.content if hasattr(result, "content") else str(result)
        
        return {"learning_plan": content}
    except Exception as e:
        # Return detailed error message for debugging
        raise HTTPException(status_code=500, detail=str(e))

# Standalone FastAPI app (for running LearningGuideAPI independently)
def create_app():
    """Create and configure a standalone FastAPI application.
    
    Creates a complete FastAPI application instance with CORS middleware,
    learning plan routing, and a root endpoint. This function is used when running
    LearningAgentAPI as an independent microservice.
    
    Returns:
        FastAPI: A configured FastAPI application instance with:
            - Title: "Learning Guide API"
            - Version: "1.0.0"
            - CORS enabled for all origins (development mode)
            - Learning plan router included
            - Root endpoint at "/"
    
    Example:
        app = create_app()
        uvicorn.run(app, host="localhost", port=8002)
    
    Note:
        CORS is configured with allow_origins=["*"] for development.
        For production, restrict origins to specific domains.
    """
    app = FastAPI(
        title="Learning Guide API",
        version="1.0.0",
        description="AI-powered personalized learning plan generation service"
    )
    
    # Enable CORS for cross-origin requests (configured for development)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # TODO: Restrict origins in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include the learning plan router
    app.include_router(router)
    
    @app.get("/")
    def root():
        """Root endpoint providing API information.
        
        Returns:
            dict: API name and available endpoints.
        """
        return {
            "message": "Learning Guide API",
            "endpoint": "/learning-plan",
            "docs": "/docs"
        }
    
    return app

# Run independently if this file is executed directly
if __name__ == "__main__":
    """Entry point for standalone execution.
    
    Starts the LearningAgentAPI as an independent microservice on port 8002.
    Access the API at: http://localhost:8002
    API documentation: http://localhost:8002/docs
    
    Usage:
        python -m api.LearningAgentAPI
    """
    app = create_app()
    print("Starting Learning Guide API on http://localhost:8002")
    print("API Documentation available at http://localhost:8002/docs")
    uvicorn.run(app, host="localhost", port=8002)