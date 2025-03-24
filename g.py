from crewai import Agent
from langchain.chat_models import ChatGroq  # Ensure you're using the correct model

llm = ChatGroq(model_name="mixtral-8x7b", api_key=os.getenv("GROQ_API_KEY"))

agent = Agent(name="Test Agent", role="writer", goal="Write about AI", llm=llm)
response = agent.execute_task("Tell me about AI.")
print(response)
