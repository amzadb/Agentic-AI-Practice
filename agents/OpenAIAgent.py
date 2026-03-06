"""OpenAI Agent - Agno Framework Implementation

This module demonstrates the use of the Agno framework with OpenAI's GPT-4o model
integrated with web search capabilities for real-time information retrieval.

About OpenAI GPT-4o:
    GPT-4o is OpenAI's most advanced model offering:
    - Superior reasoning and problem-solving capabilities
    - Excellent instruction following and task completion
    - Multimodal capabilities (text, images, etc.)
    - Industry-leading performance across benchmarks
    - Reliable tool/function calling
    
About Agno Framework:
    Agno's OpenAI integration provides:
    - Unified API consistent with other providers
    - Built-in tool orchestration (Google Search)
    - Automatic conversation management
    - Metrics tracking for token usage and costs
    - Seamless model switching between providers
    
Tools Used:
    GoogleSearchTools: Web search integration via Google Custom Search API
    - Real-time web search for current events
    - Up-to-date information beyond model's training cutoff
    - Automatically invoked when context requires it
    
Environment Setup:
    Requires in .env file:
    - OPENAI_API_KEY: For GPT-4o model access
    - GOOGLE_SEARCH_API_KEY: For Google Custom Search (optional)
    - GOOGLE_SEARCH_ENGINE_ID: Custom Search Engine ID (optional)
    
Usage:
    python agents/OpenAIAgent.py
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.googlesearch import GoogleSearchTools

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

def main():
    """Main function to run the OpenAI Agent.
    
    This function demonstrates:
    - OpenAI GPT-4o model integration via Agno
    - Google Search tool for real-time information
    - Interactive query handling with user input
    - Streaming responses for better UX
    - Automatic tool selection based on query context
    
    The agent will automatically:
    - Analyze if the query requires web search
    - Execute Google searches when needed
    - Synthesize search results with GPT-4o's reasoning
    - Present coherent, well-formatted answers
    """
    print("=== OpenAI Agent (GPT-4o) ===")
    print("This agent uses OpenAI's GPT-4o with web search capabilities.\n")
    
    # Initialize Agno Agent with OpenAI model and Google Search
    # GPT-4o: OpenAI's most capable model with excellent tool use
    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),  # OpenAI's GPT-4o via native SDK
        tools=[GoogleSearchTools()],  # Web search for current information
        markdown=True  # Enable markdown formatting in responses
    )
    
    # Show example queries to inspire users
    print("Examples of what you can ask:")
    print("- Who won the IPL-2025?")
    print("- What are the latest advancements in AI?")
    print("- Current stock price of NVIDIA")
    print("- What happened at the 2026 Winter Olympics?")
    print("- Explain quantum computing in simple terms\n")
    
    # Get query from user
    query = input("Enter your question (or press Enter for default 'Who won the IPL-2025?'): ").strip()
    
    if not query:
        query = "Who won the IPL-2025?"
        print(f"\nUsing default query: {query}\n")
    else:
        print(f"\nProcessing your question...\n")
    
    # Run the agent with the query
    # Agno orchestrates:
    # 1. Sending query to GPT-4o
    # 2. GPT-4o decides if search is needed
    # 3. Executes Google Search if necessary
    # 4. GPT-4o synthesizes final answer
    agent.print_response(query, stream=True)
    
    print("\n\n✓ Response complete!")
    
    # Optional: Show additional query option
    print("\n" + "="*60)
    while True:
        another = input("\nAsk another question? (y/n): ").strip().lower()
        if another == 'y':
            query = input("\nEnter your question: ").strip()
            if query:
                print(f"\nProcessing...\n")
                agent.print_response(query, stream=True)
                print("\n\n✓ Response complete!")
            else:
                print("No query provided.")
        else:
            print("\nGoodbye! 👋")
            break


if __name__ == "__main__":
    main()