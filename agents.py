from crewai import Agent, Task, Crew
from dotenv import load_dotenv
from tools import yt_tool
import os

# Load environment variables
load_dotenv()
import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"



# Create a senior blog content researcher agent
blog_researcher = Agent(
    role="Blog Researcher from Youtube Videos",
    goal="Get the relevant video transcription for the topic {topic} from the provided YT channel",
    verbose=True,  # Fixed typo
    memory=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science, Machine Learning, "
        "and Gen AI, and providing suggestions."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)

# Create a senior blog writer agent
blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compelling tech stories about the video {topic} from YT videos",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    llm=llm,
    allow_delegation=False
)
