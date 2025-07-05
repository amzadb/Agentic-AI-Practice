import streamlit as st

from agno.agent import Agent

from agno.models.anthropic import Claude
from agno.models.openai import OpenAIChat
from agno.models.google import Gemini
from agno.models.groq import Groq

from agno.tools.baidusearch import BaiduSearchTools
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.exa import ExaTools

from util.LoadMyKeys import load_keys
load_keys()

def MyAgent(agent, search_tool):
    # Initialize the model based on the selected agent
    if agent == "Anthropic":
        model = Claude(id="claude-sonnet-4-20250514")
    elif agent == "Open AI":
        model = OpenAIChat(id="gpt-4o")
    elif agent == "Gemini":
        model = Gemini(id="gemini-2.0-flash")
    elif agent == "Groq":
        model = Groq(id="gemma2-9b-it")

    # Initialize the search tool based on the selected option
    if search_tool == "Baidu Search":
        tool = BaiduSearchTools()
    elif search_tool == "Duck Duck Go":
        tool = DuckDuckGoTools()
    elif search_tool == "Google Search":
        tool = GoogleSearchTools()
    elif search_tool == "Exa Search":
        tool = ExaTools()
    else: 
        tool = None
        
    return Agent(
        model = model,
        tools = [tool] if tool else [],
        description = "You are a search agent that helps users find the most relevant information using Baidu.",
        instructions = [
            "Given a topic by the user, respond with the most relevant search results about that topic.",
            "Search for 3 results and select the top one unique item."
        ],
        show_tool_calls = True,
        markdown = True
    )

# --- Streamlit UI ---
st.title("AI Agent Search Application")

# Dropdowns
agent_option = st.selectbox(
    "Select AI Agent",
    ("Anthropic", "Gemini", "Groq", "Open AI")
)

search_tool_option = st.selectbox(
    "Select Search Tool",
    ("Baidu Search", "Duck Duck Go", "Exa Search", "Google Search")
)

# Prompt textarea
prompt_text = st.text_area("Enter your prompt")

# Search button
if st.button("Search"):
    if not prompt_text.strip():
        st.warning("Please enter a prompt.")
    else:
        agent = MyAgent(agent_option, search_tool_option)
        agent.print_response(prompt_text)
        result = agent.run(prompt_text).content

        # Custom CSS for tag style
        st.markdown("""
            <style>
            .tag {
                display: inline-block;
                background-color: #e0e0e0;
                color: #333;
                padding: 2px 8px;
                border-radius: 8px;
                font-size: 0.9em;
                margin: 4px;
            }
            </style>
        """, unsafe_allow_html=True)

        # Display promte text as a tag
        st.markdown(f'<span class="tag">{prompt_text}</span>', unsafe_allow_html=True)
      
        # Display the result
        st.markdown(result)