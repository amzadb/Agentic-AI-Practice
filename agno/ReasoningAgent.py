from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

from util.LoadMyKeys import load_keys
load_keys()

agent=Agent(
    model=Gemini(id="gemini-2.0-flash"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(stock_price=True, company_info=True, analyst_recommendations=True)
    ],
    instructions=[
        "Use tables to display data.",
        "Only output the report, no other text.",
    ],
    markdown=True
)

agent.print_response(
    message="Write a report on NVIDIA", 
    stream=True, 
    show_full_reasoning=True, 
    stream_intermediate_steps=True
)