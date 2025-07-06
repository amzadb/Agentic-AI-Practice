import streamlit as st

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.LoadMyKeys import load_keys
load_keys()

from util.MyLearningAgent import MyLearningAgent

# Streamlit app for personalized learning plan generation
st.title("Personalized Learning Plan Generator")

with st.form("learning_plan_form"):
    strong_skills = st.text_area("Skills you are strong at (comma-separated):")
    weak_areas = st.text_area("Areas you want to improve (comma-separated):")
    aspirations = st.text_input("Your career/learning aspirations:")
    linkedin_url = st.text_input("LinkedIn Profile URL (optional):")
    submitted = st.form_submit_button("Generate Learning Plan")

if submitted:
    with st.spinner("Generating your learning plan..."):
        prompt = (
            f"My strong skills: {strong_skills}\n"
            f"My weak areas: {weak_areas}\n"
            f"My aspirations: {aspirations}\n"
        )
        if linkedin_url:
            prompt += f"My LinkedIn profile: {linkedin_url}\n"
            prompt += (
                "Please review my LinkedIn profile and suggest improvements to make it more attractive for my aspirations. "
            )
        prompt += (
            "Please create a personalized learning plan for me. "
            "Suggest relevant YouTube videos, Udemy courses, and other resources for my weak areas and aspirations. "
            "Format the output as a step-by-step plan with links."
        )

        agent = MyLearningAgent()

        result = agent.run(prompt)
        st.markdown(result.content if hasattr(result, "content") else str(result))