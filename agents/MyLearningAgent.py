def MyLearningAgent():
    from agno.agent import Agent
    from agno.models.openai import OpenAIChat
    from agno.tools.youtube import YouTubeTools
    from agno.tools.googlesearch import GoogleSearchTools

    return Agent(
        model=OpenAIChat(id="gpt-4o"),
        tools=[YouTubeTools(), GoogleSearchTools()],
        description="You are a career coach AI that recommends learning resources and LinkedIn profile improvements.",
        markdown=True
    )