from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, writing_task
import os

os.environ["OPENAI_API_BASE"]='http://localhost:11434'
os.environ["OPENAI_MODEL_NAME"]='llama3.1'  # Adjust based on available model
os.environ["OPENAI_API_KEY"]='' # No API Key required for Ollama

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, writing_task],
    process=Process.sequential, # Optional: Sequential task execution is default
    memory=True,
    embedder={
            "provider": "ollama",
            "config":{
                "model": "all-minilm"
            }
        },
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Start the task execution process
result = crew.kickoff(inputs={"topic": "Merge Sort"})
print(result)