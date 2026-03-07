# Running the APIs

> **Important:** Run all commands from the project root directory.

---

## Option 1: Individual APIs Standalone

Run each API as an independent microservice on its own port:

### SearchAgentsAPI on port 8001:
```bash
python -m api.SearchAgentsAPI
```

**Endpoint:**
- POST `http://localhost:8001/search`

**Request body:**
```json
{
  "agent": "Anthropic",
  "search_tool": "Duck Duck Go",
  "prompt": "Anthropic Academy"
}
```

### LearningGuideAPI on port 8002:
```bash
python -m api.LearningGuideAPI
```

**Endpoint:**
- POST `http://localhost:8002/learning-plan`

**Request body:**
```json
{
  "strong_skills": "Python, Machine Learning",
  "weak_areas": "Web Development",
  "aspirations": "Become an AI Engineer",
  "linkedin_url": "https://linkedin.com/in/yourprofile"
}
```

---

## Option 2: All APIs Integrated into Main (Recommended for Production)

Run all APIs together from the main app on port 8000:

```bash
python -m api.main
```

**Alternative with auto-reload (for development):**
```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

**Endpoints:**
- POST `http://localhost:8000/search` (SearchAgentsAPI)
- POST `http://localhost:8000/learning-plan` (LearningGuideAPI)

---

## Testing with curl (Windows PowerShell)

### SearchAgentsAPI Test:
```powershell
curl -X POST http://localhost:8001/search `
  -H "Content-Type: application/json" `
  -d '{\"agent\": \"Groq\", \"search_tool\": \"duck duck go\", \"prompt\": \"What is generative AI?\"}'
```

### LearningGuideAPI Test:
```powershell
curl -X POST http://localhost:8002/learning-plan `
  -H "Content-Type: application/json" `
  -d '{\"strong_skills\": \"Python, Machine Learning\", \"weak_areas\": \"Web Development\", \"aspirations\": \"Become an AI Engineer\"}'
```

**Alternative using Invoke-RestMethod (PowerShell native):**
```powershell
# SearchAgentsAPI
$body = @{
    agent = "perplexity"
    search_tool = "duckduckgo"
    prompt = "What is generative AI?"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8001/search" -Method Post -Body $body -ContentType "application/json"

# LearningGuideAPI
$body = @{
    strong_skills = "Python, Machine Learning"
    weak_areas = "Web Development"
    aspirations = "Become an AI Engineer"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8002/learning-plan" -Method Post -Body $body -ContentType "application/json"
```

---

## Quick Reference

| Setup | Command | Port(s) | What Runs |
|-------|---------|---------|-----------|
| **Standalone Search** | `python -m api.SearchAgentsAPI` | 8001 | SearchAgentsAPI only |
| **Standalone Learning** | `python -m api.LearningGuideAPI` | 8002 | LearningGuideAPI only |
| **Both Standalone** | Both commands above (2 terminals) | 8001 + 8002 | Both APIs independently |
| **Integrated (Production)** | `python -m api.main` | 8000 | Search + Learning APIs together |

---

## How It Works

### API Structure (Both SearchAgentsAPI and LearningGuideAPI):
- **Router** (`router` variable) - Can be included in other apps via `app.include_router(router)`
- **Standalone Function** (`create_app()`) - Creates a standalone FastAPI app instance
- **Standalone Execution** (`if __name__ == "__main__"`) - Runs independently on dedicated ports
  - SearchAgentsAPI: port 8001
  - LearningGuideAPI: port 8002

This dual approach allows both APIs to be:
1. **Integrated** into main.py as routers
2. **Standalone** as independent microservices
3. **Flexible** - include, exclude, or mix as needed

---

## Common Issues & Solutions

### ModuleNotFoundError: No module named 'agents'
**Solution:** Make sure you run commands from the project root directory and use the `-m` flag:
```bash
cd "c:\Users\amzadbasha.shaik\OneDrive - iSpace\Projects\AIPractice\Agentic-AI"
python -m api.SearchAgentsAPI
python -m api.LearningGuideAPI
```

### Port Already in Use (Error 10048)
**Solution:** Kill existing Python processes:
```powershell
Get-Process python | Stop-Process -Force
```

Or check what's using the port:
```powershell
netstat -ano | findstr :8001
netstat -ano | findstr :8002
```

### CORS Issues
Both APIs have CORS enabled with `allow_origins=["*"]` for development. Configure this appropriately for production.
