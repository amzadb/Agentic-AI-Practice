# Agentic-AI

A modular, agentic AI platform for search, document processing, and generative tasks using multiple LLM providers and search tools.  
Supports both Streamlit and FastAPI interfaces.

---

## Features

- **Multi-agent support:** Gemini, OpenAI, Anthropic, Groq, and more.
- **Pluggable search tools:** Google, DuckDuckGo, Baidu, Exa, etc.
- **Document processing:** PDF, DOCX, Excel, YouTube transcripts.
- **Streamlit UI** for interactive exploration.
- **FastAPI backend** for programmatic access.
- **Environment-based key management** for secure API usage.

---

## Project Structure

```
Agentic-AI/
│
├── agno/                # Core agent and tool modules
├── api/                 # FastAPI endpoints
├── streamlit/           # Streamlit UI apps
├── util/                # Utility modules (key loading, agent wrappers, etc.)
├── requirements.txt     # Python dependencies
└── README.md
```

---

## Setup

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd Agentic-AI
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your API keys**

   - Create a `.env` file in the project root or use `util/LoadMyKeys.py` to load your keys.
   - Example `.env`:
     ```
     OPENAI_API_KEY=your_openai_key
     ANTHROPIC_API_KEY=your_anthropic_key
     GOOGLE_API_KEY=your_google_key
     GEMINI_API_KEY=your_gemini_key
     ```

---

## Usage

### **Streamlit App**

```sh
streamlit run streamlit/SearchAgents.py
```

### **FastAPI API**

```sh
uvicorn api.SearchAgentsAPI:app --reload
```
- Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

---

## Example API Request

```http
POST /search
Content-Type: application/json

{
  "agent": "Gemini",
  "search_tool": "Google Search",
  "prompt": "What is the weather in Paris?"
}
```

---

## Adding New Agents or Tools

- Add your agent/tool class in the appropriate `agno/` or `util/` module.
- Register it in the agent selection logic.

---

## Troubleshooting

- **ModuleNotFoundError:**  
  Ensure you run commands from the project root and your folder structure matches the layout above.
- **Key errors:**  
  Make sure your `.env` or key loader is set up and loaded before agent initialization.
- **Dependency errors:**  
  Run `pip install -r requirements.txt` to ensure all packages are installed.

---

## License

MIT License

---

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI](https://platform.openai.com/)
- [Anthropic](https://www.anthropic.com/)
- [Google Gemini](https://deepmind.google/technologies/gemini/)
- [Streamlit](https://streamlit.io/)
- [FastAPI](https://fastapi.tiangolo.com/)

---

*Happy hacking!*