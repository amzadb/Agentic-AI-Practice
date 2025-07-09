from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.SearchAgentsAPI import router as search_router
from api.LearningGuideAPI import router as learning_router

app = FastAPI()

# Enable CORS if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(search_router)
app.include_router(learning_router)