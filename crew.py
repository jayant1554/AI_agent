import time
import groq
from crewai import Agent, Task, Crew
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential

# Load environment variables
load_dotenv()

# Initialize Groq client
groq_client = groq.Client(api_key="YOUR_GROQ_API_KEY")

# Define a function to handle Groq API calls with retry logic
@retry(wait=wait_exponential(multiplier=1, min=2, max=10), stop=stop_after_attempt(5))
def query_groq(prompt):
    try:
        response = groq_client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200
        )
        return response.choices[0].message.content
    except groq.RateLimitError:
        print("⚠️ Rate limit exceeded! Retrying...")
        raise  # Let tenacity handle the retries
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

# Define AI Agents
researcher = Agent(
    role="AI Researcher",
    goal="Analyze AI trends and summarize findings",
    backstory="An AI expert with deep knowledge of the latest advancements",
    verbose=True,
    allow_delegation=False,
    llm=query_groq  # Using the Groq API function
)

writer = Agent(
    role="Technical Writer",
    goal="Write easy-to-understand summaries on AI",
    backstory="A skilled writer with experience in AI blogging",
    verbose=True,
    allow_delegation=False,
    llm=query_groq  # Using the Groq API function
)

# Define tasks
task_research = Task(
    description="Research the latest advancements in AI and summarize them.",
    agent=researcher,
    expected_output="A well-structured summary of the latest AI trends."
)

task_writing = Task(
    description="Write an article based on the AI research findings.",
    agent=writer,
    expected_output="A blog-style article explaining AI advancements in simple terms."
)


# Form the Crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[task_research, task_writing]
)

# Execute the Crew workflow
if __name__ == "__main__":
    results = crew.kickoff()
    print("\n📌 Final Output:\n", results)
