from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.googlesearch import GoogleSearchTools

from util.LoadMyKeys import load_keys
load_keys()

agent=Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[GoogleSearchTools()],
    markdown=True
)

agent.print_response("Who won the IPL-2025?")
# agent.print_response("What are the latest advancements in AI?")