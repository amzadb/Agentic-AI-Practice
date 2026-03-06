"""Multi-Model Search Agent - Agno Framework Implementation

This module demonstrates Agno's flexibility by creating a configurable search
agent that supports multiple LLM providers and search tools.

About Agno Framework:
    Agno is provider-agnostic, supporting all major LLM providers:
    - Anthropic (Claude): Best for nuanced reasoning and long context
    - OpenAI (GPT-4o): Most versatile and widely used
    - Google (Gemini): Fast, cost-effective with multimodal support
    - Groq: Ultra-fast inference with open-source models
    
    Key Agno Benefits:
    - Unified API: Same code works across all providers
    - Tool Integration: Pre-built search tools with consistent interface
    - Easy Switching: Change models without code refactoring
    
Supported Search Tools:
    1. BaiduSearchTools: Chinese search engine (requires API key)
    2. GoogleSearchTools: Google search (requires API key)
    3. DuckDuckGoTools: Privacy-focused search (no API key needed)
    4. ExaTools: AI-powered semantic search (requires API key)
    
Environment Setup:
    Required API keys in .env file (depending on selections):
    - ANTHROPIC_API_KEY for Claude
    - OPENAI_API_KEY for OpenAI
    - GOOGLE_API_KEY for Gemini
    - GROQ_API_KEY for Groq
    - Additional keys for search tools (except DuckDuckGo)
    
Usage:
    python agents/MySearchAgent.py
"""

from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.models.openai import OpenAIChat
from agno.models.google import Gemini
from agno.models.groq import Groq
from agno.tools.baidusearch import BaiduSearchTools
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.exa import ExaTools

from dotenv import load_dotenv
load_dotenv()  # Load API keys from .env file

def MySearchAgent(agent, search_tool):
    """Factory function to create a configurable search agent.
    
    This demonstrates Agno's provider-agnostic design:
    - Same Agent class works with all LLM providers
    - Tools integrate seamlessly regardless of model
    - Easy experimentation with different combinations
    
    Args:
        agent (str): LLM provider - "Anthropic", "Open AI", "Gemini", or "Groq"
        search_tool (str): Search engine - "Baidu Search", "Duck Duck Go", 
                          "Google Search", or "Exa Search"
    
    Returns:
        Agent: Configured Agno agent with selected model and search tool.
        
    Raises:
        ValueError: If agent selection is invalid.
    """
    # Initialize the model based on the selected agent
    # Agno's model wrappers provide unified interface to different providers
    # Agno's model wrappers provide unified interface to different providers
    if agent == "Anthropic":
        model = Claude(id="claude-sonnet-4-20250514")  # Anthropic's latest Claude model
    elif agent == "Open AI":
        model = OpenAIChat(id="gpt-4o")  # OpenAI's GPT-4o via native SDK
    elif agent == "Gemini":
        model = Gemini(id="gemini-3-flash-preview")  # Google's fast Gemini model
    elif agent == "Groq":
        model = Groq(id="qwen/qwen3-32b")  # Groq's ultra-fast inference with Qwen3
    else:
        raise ValueError("Invalid agent selected.")

    # Initialize the search tool based on the selected option
    # Agno Tools provide standardized interface across different search providers
    if search_tool == "Baidu Search":
        tool = BaiduSearchTools()  # Chinese search engine (requires API key)
    elif search_tool == "Duck Duck Go":
        tool = DuckDuckGoTools()  # Privacy-focused, no API key required
    elif search_tool == "Google Search":
        tool = GoogleSearchTools()  # Google Custom Search (requires API key)
    elif search_tool == "Exa Search":
        tool = ExaTools()  # AI-powered semantic search (requires API key)
    else:
        tool = None

    # Create Agno Agent with selected model and tool
    # Agno handles:
    # - Tool calling protocol for each LLM provider
    # - Result parsing and formatting
    # - Error handling and retries
    return Agent(
        model=model,  # Any Agno-supported model works the same way
        tools=[tool] if tool else [],  # Tools list (can be multiple)
        description="You are a search agent that helps users find the most relevant information using Baidu.",
        instructions=[
            "Given a topic by the user, respond with the most relevant search results about that topic.",
            "Search for 3 results and select the top one unique item."
        ],
        show_tool_calls=True,  # Display tool calls for transparency
        markdown=True  # Format output with markdown
    )


def main():
    """Main function to run the search agent.
    
    Demonstrates Agno's flexibility:
    - User can choose any LLM provider at runtime
    - User can choose any search tool at runtime
    - Same code works for all combinations
    
    This showcases Agno's key value proposition:
    Experiment with different models and tools without code changes.
    """
    print("=== Search Agent ===")
    print("\nAvailable Agents:")
    print("1. Anthropic")
    print("2. Open AI")
    print("3. Gemini")
    print("4. Groq")
    
    agent_choice = input("\nSelect an agent (1-4): ").strip()
    agent_map = {
        "1": "Anthropic",
        "2": "Open AI",
        "3": "Gemini",
        "4": "Groq"
    }
    agent = agent_map.get(agent_choice, "Gemini")
    
    print("\nAvailable Search Tools:")
    print("1. Baidu Search")
    print("2. Duck Duck Go")
    print("3. Google Search")
    print("4. Exa Search")
    
    tool_choice = input("\nSelect a search tool (1-4): ").strip()
    tool_map = {
        "1": "Baidu Search",
        "2": "Duck Duck Go",
        "3": "Google Search",
        "4": "Exa Search"
    }
    search_tool = tool_map.get(tool_choice, "Duck Duck Go")
    
    print(f"\nInitializing {agent} with {search_tool}...")
    
    # Create the search agent
    search_agent = MySearchAgent(agent, search_tool)
    
    # Get query from user
    query = input("\nEnter your search query: ").strip()
    
    if query:
        print(f"\nSearching for: {query}\n")
        # Run the agent with the query
        search_agent.print_response(query, stream=True)
    else:
        print("No query provided. Exiting.")


if __name__ == "__main__":
    main()