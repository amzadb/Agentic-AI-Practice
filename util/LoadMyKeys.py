import os
from dotenv import load_dotenv
load_dotenv()

def load_keys():
    os.environ["ANTHROPIC_API_KEY"]=os.getenv("ANTHROPIC_API_KEY")
    os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
    os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
    os.environ["EXA_API_KEY"]=os.getenv("EXA_API_KEY")
    os.environ['OPEN_WEATHER_API_KEY'] = os.getenv('OPEN_WEATHER_API_KEY')