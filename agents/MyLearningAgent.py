"""Learning & Career Coach Agent - Agno Framework Implementation

This module creates an AI career coach using the Agno framework with OpenAI's
GPT-4o model, integrated with YouTube and Google Search tools.

About Agno Framework:
    Agno enables building AI agents with:
    - Multi-tool orchestration (YouTube + Google Search)
    - Automatic tool selection based on user queries
    - Structured conversation management
    - Support for multiple LLM providers
    
About OpenAI Integration:
    Uses OpenAI's native SDK via Agno's OpenAIChat wrapper.
    Model: GPT-4o - OpenAI's most advanced multimodal model with:
    - Superior reasoning capabilities
    - Wide knowledge base
    - Excellent instruction following
    
Tools Available:
    1. YouTubeTools: Search and retrieve YouTube video information
    2. GoogleSearchTools: Web search for learning resources and career info
    
Environment Setup:
    Requires OPENAI_API_KEY in .env file or environment variables.
    
Usage:
    python agents/MyLearningAgent.py
"""

def MyLearningAgent():
    """Factory function to create a Learning Agent instance.
    
    Returns:
        Agent: Configured Agno agent with OpenAI model and search tools.
        
    The agent is configured as a career coach that can:
    - Search YouTube for learning videos and tutorials
    - Search the web for career resources and guidance
    - Provide personalized learning recommendations
    - Suggest LinkedIn profile improvements
    """
    from agno.agent import Agent
    from agno.models.openai import OpenAIChat
    from agno.tools.youtube import YouTubeTools
    from agno.tools.googlesearch import GoogleSearchTools

    # Initialize Agno Agent with OpenAI model and multiple tools
    # Agno automatically handles:
    # - Tool selection: Chooses YouTube vs Google based on query context
    # - Sequential tool use: Can use multiple tools to answer one query
    # - Result synthesis: Combines information from different sources
    return Agent(
        model=OpenAIChat(id="gpt-4o"),  # OpenAI's GPT-4o via native SDK
        tools=[YouTubeTools(), GoogleSearchTools()],  # Multi-tool setup
        description="You are a career coach AI that recommends learning resources and LinkedIn profile improvements.",
        markdown=True  # Format responses with markdown for better readability
    )

from dotenv import load_dotenv
load_dotenv()

def main():
    """Main function to run the Learning Agent.
    
    Demonstrates Agno agent capabilities:
    - Interactive CLI interface
    - Dynamic tool usage based on query type
    - Streaming responses for better UX
    
    Example queries:
    - "I want to learn Python" -> Uses YouTube + Google Search
    - "Improve my LinkedIn profile" -> Uses Google Search for tips
    - "Best machine learning courses" -> Uses YouTube + web search
    """
    print("=== Career Coach & Learning Agent ===")
    print("\nThis AI agent can help you with:")
    print("- Learning resource recommendations")
    print("- LinkedIn profile improvements")
    print("- Career guidance and development")
    print("\nInitializing agent...\n")
    
    # Create the learning agent
    learning_agent = MyLearningAgent()
    
    # Get query from user
    query = input("What would you like help with? (e.g., 'I want to learn Python', 'Improve my LinkedIn profile'): ").strip()
    
    if query:
        print(f"\nProcessing your request...\n")
        # Run the agent with the query
        learning_agent.print_response(query, stream=True)
    else:
        print("No query provided. Exiting.")


if __name__ == "__main__":
    main()