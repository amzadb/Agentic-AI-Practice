import random

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool

from keys import load_my_keys
load_my_keys()

@tool(show_result=True, stop_after_tool_call=True)
def get_weather(city: str) -> str:
    """Get the weather for a city."""
    # In a real implementation, this would call a weather API
    weather_conditions = ["sunny", "cloudy", "rainy", "snowy", "windy"]
    random_weather = random.choice(weather_conditions)

    return f"The weather in {city} is {random_weather}."

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[get_weather],
    markdown=True,
)
agent.print_response("What is the weather in Hyderabad, India?", stream=True)