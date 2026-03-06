"""Gemini Agent - Agno Framework Implementation

This module demonstrates the use of the Agno framework with Google's Gemini model
integrated with web search capabilities.

About Gemini:
    Google's Gemini is a family of multimodal AI models offering:
    - Fast inference with Gemini 2.0 Flash variant
    - Cost-effective pricing for high-volume applications
    - Strong performance on reasoning and knowledge tasks
    - Native multimodal capabilities (text, images, etc.)
    
About Agno Framework:
    Agno's Gemini integration provides:
    - Unified API consistent with other providers
    - Built-in tool orchestration (Google Search)
    - Automatic conversation management
    - Seamless model switching capability
    
Tools Used:
    GoogleSearchTools: Web search integration via Google Custom Search API
    - Real-time web search results
    - Provides current information beyond training data
    - Automatically invoked when needed
    
Environment Setup:
    Requires in .env file:
    - GOOGLE_API_KEY: For Gemini model access
    - GOOGLE_SEARCH_API_KEY: For Google Custom Search API (optional)
    - GOOGLE_SEARCH_ENGINE_ID: Custom Search Engine ID (optional)
    
Usage:
    python agents/GeminiAgent.py
"""

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.googlesearch import GoogleSearchTools

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

def main():
    """Main function to run the Gemini Agent.
    
    This function demonstrates:
    - Gemini 2.0 Flash model integration via Agno
    - Google Search tool for real-time information
    - Interactive query handling
    - Streaming responses for better UX
    
    The agent will automatically:
    - Determine when web search is needed
    - Execute Google searches if required
    - Synthesize search results into coherent answers
    """
    print("=== Gemini Agent (Gemini 2.0 Flash) ===")
    print("This agent uses Google's Gemini model with web search capabilities.\n")
    
    # Initialize Agno Agent with Gemini model and Google Search
    # Gemini 2.0 Flash: Fast, cost-effective, with good reasoning
    agent = Agent(
        model=Gemini(id="gemini-2.0-flash"),  # Google's fast Gemini variant
        tools=[GoogleSearchTools()],  # Web search capability
        markdown=True  # Enable markdown formatting in responses
    )
    
    # Show example queries
    print("Examples of what you can ask:")
    print("- Who won the IPL-2025?")
    print("- What is the latest news about AI?")
    print("- Current stock price of Tesla")
    print("- What happened in the 2026 Olympics?\n")
    
    # Get query from user
    query = input("Enter your question (or press Enter for default 'Who won the IPL-2025?'): ").strip()
    
    if not query:
        query = "Who won the IPL-2025?"
        print(f"\nUsing default query: {query}\n")
    else:
        print(f"\nProcessing your question...\n")
    
    # Run the agent with the query
    # Agno will automatically decide if web search is needed
    agent.print_response(query, stream=True)
    
    print("\n\n✓ Response complete!")


if __name__ == "__main__":
    main()