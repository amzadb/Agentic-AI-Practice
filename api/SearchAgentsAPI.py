from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from util.MySearchAgent import MySearchAgent
from util.LoadMyKeys import load_keys
load_keys()

app = FastAPI()

# Optional: Enable CORS if you want to call this API from a frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchRequest(BaseModel):
    agent: str
    search_tool: str
    prompt: str

# Define the API endpoint for search
@app.post("/search")
def search(request: SearchRequest):
    try:
        agent = MySearchAgent(request.agent, request.search_tool)
        result = agent.run(request.prompt)
        # If result has .content, return it; else, return str(result)
        content = getattr(result, "content", str(result))
        return {
            "prompt": request.prompt,
            "result": content
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))