from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.LoadMyKeys import load_keys
from agents.MySearchAgent import MySearchAgent

load_keys()

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