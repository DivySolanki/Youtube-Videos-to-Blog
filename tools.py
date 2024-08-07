from crewai_tools import YoutubeChannelSearchTool


# Initialize the tool with a specific Youtube channel handel to target search
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle="@takeUforward",
    config=dict(
        llm=dict(
            provider="ollama",
            config=dict(
                model="llama3.1"
            ),
        ),
        embedder=dict(
            provider="ollama",
            config=dict(
                model="all-minilm"
            ),
        ),
    )
)


