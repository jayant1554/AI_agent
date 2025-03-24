from crewai import Task
from tools import yt_tool  # Importing the YouTube search tool

# Research Task
research_task = Task(
    name="YouTube Data Science Research",
    description="Identify and analyze videos related to Data Science on the @krishnaik06 YouTube channel.",
    agent=None,  # Assign this to the appropriate agent in your setup
    expected_output="A list of key insights extracted from relevant YouTube videos.",
    tool=yt_tool,
    inputs={'search_query': 'Data Science'}  # ✅ Corrected key
)

# Writing Task
write_task = Task(
    name="Blog Writing",
    description="Write a blog post summarizing the key insights from YouTube research.",
    agent=None,  # Assign this to the appropriate agent in your setup
    expected_output="A well-structured blog post on Data Science.",
    inputs={'research_summary': 'This will be filled by the research task.'}
)
