import streamlit as st

from agno.agent import Agent

from agno.models.openai import OpenAIChat
from agno.models.google import Gemini
from agno.models.groq import Groq

from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.duckduckgo import DuckDuckGoTools

from util.LoadMyKeys import load_keys
load_keys()

def SearchTools(search_tool):
    if search_tool == "Duck Duck Go":
        return DuckDuckGoTools()
    if search_tool == "Google Search":
        return GoogleSearchTools()
    
def OpenAIAgent(prompt, search_tool):
    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        tools=[SearchTools(search_tool)],
        markdown=True
    )
    agent.print_response(prompt)
    return agent.run(prompt).content
    # return f"**OpenAI Agent** used with **{search_tool}**.\n\nPrompt: {prompt}\n\n_Result: This is a sample response from OpenAI Agent._"

def GeminiAgent(prompt, search_tool):
    agent=Agent(
        model=Gemini(id="gemini-2.0-flash"),
        tools=[SearchTools(search_tool)],
        markdown=True
    )
    agent.print_response(prompt)
    return agent.run(prompt).content
    # return f"**Gemini Agent** used with **{search_tool}**.\n\nPrompt: {prompt}\n\n_Result: This is a sample response from Gemini Agent._"

def GroqAgent(prompt, search_tool):
    agent = Agent(
        model=Groq(id="gemma2-9b-it"),
        tools=[SearchTools(search_tool)],
        markdown=True
    )
    agent.print_response(prompt)
    return agent.run(prompt).content
    # return f"**Groq Agent** used with **{search_tool}**.\n\nPrompt: {prompt}\n\n_Result: This is a sample response from Groq Agent._"

# --- Streamlit UI ---
st.title("AI Agent Search Application")

# Dropdowns
agent_option = st.selectbox(
    "Select AI Agent",
    ("Google Gemini", "Groq", "Open AI")
)

search_tool_option = st.selectbox(
    "Select Search Tool",
    ("Duck Duck Go", "Google Search")
    # , "Microsoft Bing", "Yahoo!")
)

# Prompt textarea
prompt_text = st.text_area("Enter your prompt")

# Search button
if st.button("Search"):
    if not prompt_text.strip():
        st.warning("Please enter a prompt.")
    else:
        if agent_option == "Open AI":
            result = OpenAIAgent(prompt_text, search_tool_option)
        elif agent_option == "Google Gemini":
            result = GeminiAgent(prompt_text, search_tool_option)
        elif agent_option == "Groq":
            result = GroqAgent(prompt_text, search_tool_option)
        else:
            result = "Invalid agent selected."

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
        st.markdown(result)