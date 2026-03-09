"""
SQLiteDBAgent - Database Interaction Agent

This module implements an intelligent agent for interacting with SQLite databases.
It leverages the Agno framework and OpenAI's GPT-4o model to execute SQL queries,
perform CRUD operations, and provide structured responses from database queries.

Module Features:
    - Connects to SQLite databases using SQLTools
    - Uses GPT-4o for natural language to SQL translation
    - Executes complex database queries intelligently
    - Returns results in structured, markdown-formatted output
    - Shows detailed SQL query execution logs for transparency

Database:
    - Primary database: Chinook_Sqlite.sqlite (located in the agents directory)
    - Database URL is resolved using absolute paths for reliability
    
Usage:
    Run this script directly to execute predefined database queries:
    
    python agents/SQLiteDBAgent.py
    
    The agent will respond to the configured prompts and display:
    - All tables and their schemas in the database
    - Data from specific queries based on provided instructions

Example Queries:
    - Show database structure and available tables
    - List all records from specific tables
    - Perform CRUD operations (Create, Read, Update, Delete)
    - Execute complex SQL joins and aggregations
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.sql import SQLTools
import os
from dotenv import load_dotenv

# Load environment variables from .env file (contains API keys)
load_dotenv()

# ============================================================================
# Database Configuration
# ============================================================================
# Construct the absolute path to the SQLite database file
# This ensures the database is found regardless of where the script is executed
db_path = os.path.join(os.path.dirname(__file__), "Chinook_Sqlite.sqlite")
# Convert to SQLite URL format (handles Windows backslashes)
db_url = f"sqlite:///{db_path.replace(chr(92), '/')}"

# ============================================================================
# Agent Initialization
# ============================================================================
# Create an intelligent SQLite agent configured with:
#   - OpenAI's GPT-4o model for advanced reasoning and SQL generation
#   - SQLTools for database connectivity and query execution
#   - Detailed instructions for structured outputs
agent = Agent(
    name="SQLiteDBAgent",
    role="Interact with SQLite database to perform CRUD operations",
    model=OpenAIChat(id="gpt-4o"),
    tools=[SQLTools(db_url=db_url)],
    instructions="Use SQL queries to interact with the database. Always return results in a structured format.",
    show_tool_calls=True,  # Display SQL queries being executed
    markdown=True,  # Format responses in markdown for readability
)

# ============================================================================
# Execute Database Queries
# ============================================================================
# Query the database to retrieve all tables and their schemas
agent.print_response("Show me all tables in the database and their schemas")
# agent.print_response("List all artists in the database")
# agent.print_response("List the employees from the database")
# agent.print_response("Insert a new employee with first name 'Arsahd', last name 'Afsar', title 'AI Engineer' and email 'kireeti.s@gmail.com'")