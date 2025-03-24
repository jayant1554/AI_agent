from crewai_tools import YoutubeChannelSearchTool

# Initialize the YouTube search tool with the correct input format
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle="@krishnaik06",
    search_query="Data Science"  # ✅ Ensuring the correct key
)
