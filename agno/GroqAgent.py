from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

from keys import load_my_keys
load_my_keys()

agent=Agent(
    model=Groq(id="gemma2-9b-it"),
    tools=[DuckDuckGoTools()],
    markdown=True
)

agent.print_response("Who won the IPL-2025?")