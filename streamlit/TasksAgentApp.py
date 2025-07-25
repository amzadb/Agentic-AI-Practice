import streamlit as st

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.TasksAgent import summarize_tasks

st.title("Task Classification Agent")

tasks_input = st.text_area("Paste your tasks here (one per line):", height=200)
uploaded_file = st.file_uploader("Or upload a tasks file (.txt)", type=["txt"])

if uploaded_file:
    tasks_input = uploaded_file.read().decode("utf-8")

if st.button("Classify Tasks"):
    if tasks_input.strip():
        with st.spinner("Classifying tasks..."):
            summary = summarize_tasks(tasks_input)
        st.subheader("Tasks Summary")
        st.markdown(summary)
    else:
        st.warning("Please enter tasks or upload a file.")