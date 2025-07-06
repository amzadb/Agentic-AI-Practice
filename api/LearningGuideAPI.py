from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.LoadMyKeys import load_keys
from agents.MyLearningAgent import MyLearningAgent

load_keys()

app = FastAPI()

# Optional: Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LearningPlanRequest(BaseModel):
    strong_skills: str
    weak_areas: str
    aspirations: str
    linkedin_url: str = None

@app.post("/learning-plan")
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