from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.sql import SQLTools

from keys import load_my_keys
load_my_keys()

# Agent with SQLite database tools
agent = Agent(
    name="SQLiteDBAgent",
    role="Interact with SQLite database to perform CRUD operations",
    model=OpenAIChat(id="gpt-4o"),
    tools=[SQLTools(db_url="sqlite:///Chinook_Sqlite.sqlite")],
    instructions="Use SQL queries to interact with the database. Always return results in a structured format.",
    show_tool_calls=True,
    markdown=True,
)

# agent.print_response("Show me all tables in the database and their schemas")
# agent.print_response("List all artists in the database")
agent.print_response("List the employees from the database")
# agent.print_response("Insert a new employee with first name 'Kireeti', last name 'S', title 'AI Engineer' and email 'kireeti.s@gmail.com'")