from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from agents.MySearchAgent import MySearchAgent

from dotenv import load_dotenv
load_dotenv()  # Load API keys from .env file

router = APIRouter()

class SearchRequest(BaseModel):
    agent: str
    search_tool: str
    prompt: str

@router.post("/search")
def search(request: SearchRequest):
    try:
        agent = MySearchAgent(request.agent, request.search_tool)
        result = agent.run(request.prompt)
        content = getattr(result, "content", str(result))
        return {
            "prompt": request.prompt,
            "result": content
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Standalone FastAPI app (for running SearchAgentsAPI independently)
def create_app():
    """Create and return a standalone FastAPI app"""
    app = FastAPI(title="Search Agents API", version="1.0.0")
    
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
        return {"message": "Search Agents API", "endpoint": "/search"}
    
    return app

# Run independently if this file is executed directly
if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="localhost", port=8001)