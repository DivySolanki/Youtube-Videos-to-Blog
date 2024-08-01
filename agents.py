from crewai import Agent
from tools import yt_tool

## Create a senior blog content researcher

blog_researcher = Agent(
    role="Blog Researcher from YouTube Videos",
    goal="get the relevant video content for the topic {topic} from Yt channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in Computer Science discipline particularly specialized in Data Structures and Algorithms, also it provides suggestions"
    ),
    tools=[yt_tool],
    allow_delegation=True
)

## Creating a senior blog writer agent with YT tool

blog_writer = Agent(
    role="Writer",
    goal="Narrate a compelling tech stories about the video {topic} from Yt channel",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives that capture and educate, bringing new discoveries to the lime light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False
)

