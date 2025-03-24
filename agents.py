from crewai import Agent, Task, Crew
from dotenv import load_dotenv
from tools import yt_tool
import os

# Load environment variables

load_dotenv()

from pydantic import field_validator

# Ensure the Groq API key is correctly set
os.environ["GROQ_API_KEY"] = "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"
os.environ["GROQ_PROVIDER"] = "groq/llama3-8b-8192"

# Explicitly define the LLM model
llm_model = "groq/llama3-8b-8192"

# Create a senior blog content researcher agent
blog_researcher = Agent(
    role="Blog Researcher from Youtube Videos",
    goal="Get the relevant video transcription for the topic {topic} from the provided YT channel",
    verbose=True,  

    provider="groq",
    llm=llm_model,  # Explicitly using the LLM parameter
    memory=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science, Machine Learning, "
        "and Gen AI, and providing suggestions."
    ),
    tools=[yt_tool],
    allow_delegation=True
)

# Create a senior blog writer agent
blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compelling tech stories about the video {topic} from YT videos",
    verbose=True,
    memory=True,
    provider="groq",
    llm=llm_model,  # Explicitly using the LLM parameter
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    allow_delegation=False
)
