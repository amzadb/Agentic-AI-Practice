"""Groq Agent - Agno Framework Implementation

This module demonstrates the use of the Agno framework to create an AI agent
powered by Groq's Qwen3-32B model with web search capabilities.

About Agno Framework:
    Agno is a Python framework for building AI agents that can use tools,
    manage conversations, and integrate with multiple LLM providers.
    
    Key Components:
    - Agent: Core class that orchestrates model, tools, and instructions
    - Models: Wrappers for various LLM providers (OpenAI, Anthropic, Groq, Gemini)
    - Tools: Pre-built integrations for search, APIs, and custom functions
    
About Groq:
    Groq provides ultra-fast LLM inference with various open-source models.
    This agent uses Qwen3-32B, a powerful multilingual model from Alibaba.
    
Tools Used:
    - DuckDuckGoTools: Web search capability without API keys
    
Environment Setup:
    Requires GROQ_API_KEY in .env file or environment variables.
    
Usage:
    python agents/GroqAgent.py
"""

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

# Initialize Agno Agent with Groq model
# Agno Agent is the core orchestrator that:
# 1. Manages the LLM model (Groq's Qwen3-32B in this case)
# 2. Integrates tools (DuckDuckGo search)
# 3. Handles conversation flow and tool calling
agent = Agent(
    model=Groq(id="qwen/qwen3-32b"),  # Groq's fast inference with Qwen3-32B model
    tools=[DuckDuckGoTools()],  # Web search capability via DuckDuckGo
    markdown=True  # Enable markdown formatting in responses
)

def main():
    """Main function to run the Groq Agent.
    
    This function demonstrates:
    - Interactive user input for queries
    - Agent invocation with print_response()
    - Streaming responses for real-time output
    
    The agent will automatically:
    - Determine if web search is needed
    - Call DuckDuckGo search tool when necessary
    - Synthesize search results into a coherent answer
    """
    print("=== Groq Agent (Qwen3-32B) ===")
    print("This agent uses DuckDuckGo search to answer your questions.\n")
    
    # Get query from user
    query = input("Enter your question (or press Enter for default 'Who won the IPL-2025?'): ").strip()
    
    if not query:
        query = "Who won the IPL-2025?"
        print(f"\nUsing default query: {query}\n")
    else:
        print(f"\nProcessing your question...\n")
    
    # Run the agent with the query
    # print_response() is Agno's main execution method:
    # - Sends query to the LLM
    # - Handles tool calls automatically
    # - Streams output in real-time when stream=True
    agent.print_response(query, stream=True)


if __name__ == "__main__":
    main()