from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.googlesearch import GoogleSearchTools

from util.LoadMyKeys import load_keys
load_keys()

agent=Agent(
    model=Gemini(id="gemini-2.0-flash"),
    tools=[GoogleSearchTools()],
    markdown=True
)

agent.print_response("Who won the IPL-2025?")