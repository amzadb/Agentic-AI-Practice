import os
from dotenv import load_dotenv
load_dotenv()

def load_keys():
    os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
    os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
    os.environ["EXA_API_KEY"]=os.getenv("EXA_API_KEY")