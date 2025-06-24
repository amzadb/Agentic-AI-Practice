import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI()

def read_tasks(file_path):
    tasks = []
    with open(file_path, 'r') as file:
        return file.read()
    
def summarize_tasks(tasks):
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
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    file_path = "./langchain/tasks.txt"  # Path to your tasks file
    tasks = read_tasks(file_path)
    summary = summarize_tasks(tasks)
    print("Tasks Summary:")
    print(summary)