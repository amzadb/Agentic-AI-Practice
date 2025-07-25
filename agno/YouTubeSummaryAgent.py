from agno.agent import Agent
from agno.tools.youtube import YouTubeTools

from keys import load_my_keys
load_my_keys()

agent = Agent(
    model="gemini-2.0-flash",
    name="YouTubeSummaryAgent",
    tools=[YouTubeTools()],
    show_tool_calls=True,
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
)

agent.print_response("Summarize this video https://www.youtube.com/watch?v=FLYcpeYLJFI&list=PL3JVwFmb_BnTItOu5wk67Vb2lrp2zMb2o", markdown=True)