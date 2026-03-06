"""DeepSeek Agent - Agno Framework Implementation

This module demonstrates the use of the Agno framework with DeepSeek models,
an open-source alternative to proprietary LLMs with competitive performance.

About DeepSeek:
    DeepSeek is an emerging AI model provider offering:
    - Cost-effective inference compared to GPT-4
    - Strong reasoning capabilities
    - Open-source alternative to proprietary models
    - Support for various tasks including coding, writing, and analysis
    
About Agno Framework:
    Agno's DeepSeek integration provides:
    - Unified API consistent with other providers
    - Easy switching between DeepSeek and other models
    - Built-in conversation management
    - Metrics tracking and monitoring
    
Model Configuration:
    DeepSeek(): Uses the default DeepSeek model
    - No tools configured (pure text generation)
    - Suitable for creative writing, reasoning, and general tasks
    
Environment Setup:
    Requires DEEPSEEK_API_KEY in .env file or environment variables.
    Get your API key from: https://platform.deepseek.com/
    
Usage:
    python agents/DeepSeekAgent.py
"""

from agno.agent import Agent, RunResponse
from agno.models.deepseek import DeepSeek

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

def main():
    """Main function to run the DeepSeek Agent.
    
    This function demonstrates:
    - DeepSeek model integration via Agno
    - Interactive user prompts
    - Creative text generation
    - Streaming responses for real-time output
    
    DeepSeek excels at:
    - Creative writing (stories, poetry, etc.)
    - Reasoning tasks
    - Code generation
    - General Q&A
    """
    print("=== DeepSeek Agent ===")
    print("This agent uses DeepSeek model for creative text generation.\n")
    
    # Initialize Agno Agent with DeepSeek model
    # DeepSeek offers cost-effective inference with strong performance
    agent = Agent(
        model=DeepSeek(),  # Uses default DeepSeek model
        markdown=True  # Enable markdown formatting in responses
    )
    
    # Get prompt from user
    print("Examples of what you can ask:")
    print("- Share a 2 sentence horror story")
    print("- Write a haiku about AI")
    print("- Explain quantum computing simply")
    print("- Create a Python function to sort a list\n")
    
    user_prompt = input("Enter your prompt (or press Enter for default horror story): ").strip()
    
    if not user_prompt:
        user_prompt = "Share a 2 sentence horror story."
        print(f"\nUsing default prompt: {user_prompt}\n")
    else:
        print(f"\nProcessing your request...\n")
    
    # Print the response in the terminal
    # Agno handles the API call, streaming, and formatting automatically
    agent.print_response(user_prompt, stream=True)
    
    print("\n\n✓ Response complete!")


if __name__ == "__main__":
    main()