from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.sql import SQLTools

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

# Get the absolute path to the database file
import os
db_path = os.path.join(os.path.dirname(__file__), "Chinook_Sqlite.sqlite")
db_url = f"sqlite:///{db_path.replace(chr(92), '/')}"

# Agent with SQLite database tools
agent = Agent(
    name="SQLiteDBAgent",
    role="Interact with SQLite database to perform CRUD operations",
    model=OpenAIChat(id="gpt-4o"),
    tools=[SQLTools(db_url=db_url)],
    instructions="Use SQL queries to interact with the database. Always return results in a structured format.",
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Show me all tables in the database and their schemas")
# agent.print_response("List all artists in the database")
# agent.print_response("List the employees from the database")
# agent.print_response("Insert a new employee with first name 'Arsahd', last name 'Afsar', title 'AI Engineer' and email 'kireeti.s@gmail.com'")