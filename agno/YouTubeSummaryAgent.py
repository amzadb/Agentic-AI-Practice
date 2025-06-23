from agno.agent import Agent
from agno.tools.youtube import YouTubeTools

import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

agent = Agent(
    tools=[YouTubeTools()],
    show_tool_calls=True,
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
)

agent.print_response("Summarize this video https://www.youtube.com/watch?v=FLYcpeYLJFI&list=PL3JVwFmb_BnTItOu5wk67Vb2lrp2zMb2o", markdown=True)