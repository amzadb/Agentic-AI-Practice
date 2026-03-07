from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.SearchAgentsAPI import router as search_router
from api.LearningAgentAPI import router as learning_router

app = FastAPI(title="AI Agents API", version="1.0.0")

# Enable CORS if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
# Search Agents API Router (default: INCLUDED)
app.include_router(search_router, prefix="", tags=["search"])

# Learning Guide API Router (default: INCLUDED)
app.include_router(learning_router, prefix="", tags=["learning"])

@app.get("/")
def root():
    return {
        "message": "AI Agents API",
        "endpoints": {
            "search": "/search",
            "learning_plan": "/learning-plan"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)