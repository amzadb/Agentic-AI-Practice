"""
AudioAgent - Audio Analysis and Understanding Agent

This module implements an intelligent agent capable of analyzing and understanding
audio content using OpenAI's advanced audio processing models. It leverages the
Agno framework to process audio files and generate natural language descriptions
of audio content.

Module Features:
    - Downloads audio files from remote URLs
    - Converts audio to base64 encoding for API transmission
    - Uses OpenAI's gpt-4o-audio-preview model for audio understanding
    - Generates detailed natural language descriptions of audio
    - Supports WAV audio format

Audio Models:
    - gpt-4o-audio-preview: Advanced multimodal model that understands audio
      and can describe what it hears, identify speakers, sounds, music, etc.

Usage:
    Run this script directly to analyze a sample audio file:
    
    python agents/AudioAgent.py
    
    The agent will:
    1. Download a sample WAV audio file from OpenAI's servers
    2. Analyze the audio content
    3. Provide a detailed description of what is in the audio

Example Capabilities:
    - Identify background sounds and music
    - Detect speech and speaker characteristics
    - Describe environmental audio
    - Analyze tone and emotion in voice
    - Understand context from audio content

Environment Requirements:
    - OPENAI_API_KEY: Set in .env file for OpenAI API access
"""

import base64
import requests
from agno.agent import Agent, RunResponse  # noqa
from agno.media import Audio
from agno.models.openai import OpenAIChat

# ============================================================================
# Environment Setup
# ============================================================================
# Load environment variables from .env file (contains OpenAI API key)
from dotenv import load_dotenv
load_dotenv()

# ============================================================================
# Audio Data Retrieval
# ============================================================================
# Fetch sample audio file from OpenAI's CDN
# This is a WAV format audio file used for demonstration
url = "https://openaiassets.blob.core.windows.net/$web/API/docs/audio/alloy.wav"
response = requests.get(url)
response.raise_for_status()  # Raise an exception for HTTP errors

# Extract binary audio data from the response
wav_data = response.content

# ============================================================================
# Agent Initialization
# ============================================================================
# Create an audio analysis agent configured with:
#   - gpt-4o-audio-preview: OpenAI's model optimized for audio understanding
#   - Text output modality for generating natural language descriptions
#   - Markdown formatting for readable output
agent = Agent(
    model=OpenAIChat(
        id="gpt-4o-audio-preview",
        modalities=["text"]  # Generate text output from audio analysis
    ),
    markdown=True,  # Format responses in markdown for readability
)

# ============================================================================
# Audio Analysis Execution
# ============================================================================
# Send the audio to the agent with a query about its content
# The agent will analyze the audio and provide a detailed description
agent.print_response(
    "What is in this audio?", 
    audio=[
        Audio(content=wav_data, format="wav")
    ]
)