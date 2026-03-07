from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from agents.MyLearningAgent import MyLearningAgent

from dotenv import load_dotenv
load_dotenv()  # Load API keys from .env file

router = APIRouter()

class LearningPlanRequest(BaseModel):
    strong_skills: str
    weak_areas: str
    aspirations: str
    linkedin_url: str = None

@router.post("/learning-plan")
def generate_learning_plan(request: LearningPlanRequest):
    try:
        prompt = (
            f"My strong skills: {request.strong_skills}\n"
            f"My weak areas: {request.weak_areas}\n"
            f"My aspirations: {request.aspirations}\n"
        )
        if request.linkedin_url:
            prompt += f"My LinkedIn profile: {request.linkedin_url}\n"
            prompt += (
                "Please review my LinkedIn profile and suggest improvements to make it more attractive for my aspirations. "
            )
        prompt += (
            "Please create a personalized learning plan for me. "
            "Suggest relevant YouTube videos, Udemy courses, and other resources for my weak areas and aspirations. "
            "Format the output as a step-by-step plan with links."
        )

        agent = MyLearningAgent()
        result = agent.run(prompt)
        content = result.content if hasattr(result, "content") else str(result)
        return {"learning_plan": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Standalone FastAPI app (for running LearningGuideAPI independently)
def create_app():
    """Create and return a standalone FastAPI app"""
    app = FastAPI(title="Learning Guide API", version="1.0.0")
    
    # Enable CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include the router
    app.include_router(router)
    
    @app.get("/")
    def root():
        return {"message": "Learning Guide API", "endpoint": "/learning-plan"}
    
    return app

# Run independently if this file is executed directly
if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="localhost", port=8002)