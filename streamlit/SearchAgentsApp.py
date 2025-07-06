import streamlit as st

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.LoadMyKeys import load_keys
load_keys()

from agents.MySearchAgent import MySearchAgent

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
        agent = MySearchAgent(agent_option, search_tool_option)
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