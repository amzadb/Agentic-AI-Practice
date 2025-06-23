from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

from util.LoadMyKeys import load_keys
load_keys()

agent=Agent(
    model=Groq(id="gemma2-9b-it"),
    tools=[DuckDuckGoTools()],
    markdown=True
)

agent.print_response("Who won the IPL-2025?")