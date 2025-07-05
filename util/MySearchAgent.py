
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.models.openai import OpenAIChat
from agno.models.google import Gemini
from agno.models.groq import Groq
from agno.tools.baidusearch import BaiduSearchTools
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.exa import ExaTools

def MySearchAgent(agent, search_tool):
    # Initialize the model based on the selected agent
    if agent == "Anthropic":
        model = Claude(id="claude-sonnet-4-20250514")
    elif agent == "Open AI":
        model = OpenAIChat(id="gpt-4o")
    elif agent == "Gemini":
        model = Gemini(id="gemini-2.0-flash")
    elif agent == "Groq":
        model = Groq(id="gemma2-9b-it")
    else:
        raise ValueError("Invalid agent selected.")

    # Initialize the search tool based on the selected option
    if search_tool == "Baidu Search":
        tool = BaiduSearchTools()
    elif search_tool == "Duck Duck Go":
        tool = DuckDuckGoTools()
    elif search_tool == "Google Search":
        tool = GoogleSearchTools()
    elif search_tool == "Exa Search":
        tool = ExaTools()
    else:
        tool = None

    return Agent(
        model=model,
        tools=[tool] if tool else [],
        description="You are a search agent that helps users find the most relevant information using Baidu.",
        instructions=[
            "Given a topic by the user, respond with the most relevant search results about that topic.",
            "Search for 3 results and select the top one unique item."
        ],
        show_tool_calls=True,
        markdown=True
    )