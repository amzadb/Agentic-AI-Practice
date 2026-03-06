"""Task Prioritization Agent - Native OpenAI SDK Implementation

This module demonstrates using OpenAI's native Python SDK directly (not Agno)
to create a task categorization and prioritization system.

About OpenAI SDK:
    This uses OpenAI's official Python client library directly:
    - Direct API calls via openai.OpenAI() client
    - Full control over request parameters
    - No framework abstraction layer
    
    OpenAI SDK vs Agno:
    - OpenAI SDK: Direct API access, more control, vendor-specific code
    - Agno: Multi-provider support, tool orchestration, higher abstraction
    
Model Used:
    GPT-4o: OpenAI's most capable model with:
    - Advanced reasoning for task prioritization
    - Excellent instruction following
    - Structured output capabilities
    
Functionality:
    Reads tasks from a file and categorizes them into:
    - High Priority: Urgent and critical tasks
    - Medium Priority: Important but not urgent
    - Low Priority: Neither urgent nor important
    
Environment Setup:
    Requires OPENAI_API_KEY in .env file or environment variables.
    
Usage:
    python agents/TasksAgent.py
"""

from dotenv import load_dotenv
load_dotenv()  # Load OPENAI_API_KEY from .env

# Using OpenAI's native SDK (not Agno framework)
from openai import OpenAI
client = OpenAI()  # Initializes with OPENAI_API_KEY from environment

def read_tasks(file_path):
    """Read tasks from a text file.
    
    Args:
        file_path (str): Path to the tasks file.
        
    Returns:
        str: Content of the tasks file.
    """
    tasks = []
    with open(file_path, 'r') as file:
        return file.read()
    
def summarize_tasks(tasks):
    """Categorize and prioritize tasks using OpenAI's GPT-4o.
    
    This function demonstrates:
    - Native OpenAI SDK usage (vs Agno framework)
    - Prompt engineering for structured output
    - Direct chat completions API call
    
    Args:
        tasks (str): Text containing list of tasks to categorize.
        
    Returns:
        str: Formatted categorized tasks (High/Medium/Low priority).
        
    Note:
        This uses OpenAI's Chat Completions API directly.
        For multi-provider support, consider using Agno framework instead.
    """
    # Construct detailed prompt for GPT-4o
    # Prompt engineering: Clear instructions + format specification
    prompt = f"""
    You are a smart task planning agent.
    Given a list of tasks, categorize them into 3 priorities: High, Medium, and Low.
    - High Priority: Tasks that are urgent and critical.
    - Medium Priority: Tasks that are important but not urgent.
    - Low Priority: Tasks that are neither urgent nor important.
    
    Tasks:
    {tasks}
    
    Return the response in the following format:
    High Priority:
    - Task 1
    - Task 2
    Medium Priority:
    - Task 3
    - Task 4
    Low Priority:
    - Task 5
    - Task 6
    """
    # Direct OpenAI API call using native SDK
    # This is lower-level than Agno's Agent.print_response()
    response = client.chat.completions.create(
        model="gpt-4o",  # OpenAI's latest model
        messages=[{"role": "user", "content": prompt}],  # Chat format
        max_tokens=150  # Limit response length
    )
    # Extract and return the model's response
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    """Main execution block.
    
    Demonstrates native OpenAI SDK workflow:
    1. Read input from file
    2. Construct prompt
    3. Call OpenAI API
    4. Display results
    
    Compare this with Agno's approach:
    - Agno: agent.print_response(query) handles everything
    - Native SDK: Manual prompt construction and API calls
    
    Choose based on needs:
    - Use Agno: For tool integration, multi-provider support
    - Use Native SDK: For fine-grained control, simple use cases
    """
    file_path = "./agents/tasks.txt"  # Path to your tasks file
    tasks = read_tasks(file_path)
    summary = summarize_tasks(tasks)
    print("Tasks Summary:")
    print(summary)