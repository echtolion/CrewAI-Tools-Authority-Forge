from crewai_tools import tool
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from llmware.models import ModelCatalog
import os
import logging
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

@tool("YouTube Comment Sentiment Analysis Tool")
def analyze_comments(video_id: str) -> list:
    """
    Analyzes sentiments of YouTube comments using the SLIM sentiment analysis tool.
    Parameters:
        video_id (str): The YouTube video ID whose comments are to be analyzed.
    Returns:
        list: List of tuples containing comment ID, comment text, and sentiment score.
    """
    try:
        credentials_path = os.getenv('GOOGLE_CREDS_JSON_PATH')
        if not credentials_path:
            raise FileNotFoundError("Google credentials path not found in environment variables.")
        
        credentials = Credentials.from_authorized_user_file(credentials_path)
        youtube = build('youtube', 'v3', credentials=credentials)
        sentiment_tool = ModelCatalog().tool_test_run("slim-sentiment-tool")
        
        request = youtube.commentThreads().list(part="snippet", videoId=video_id, textFormat="plainText")
        response = request.execute()
        analyzed_comments = []

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comment_id = item['id']
            sentiment_result = sentiment_tool.analyze_text(comment)
            analyzed_comments.append((comment_id, comment, sentiment_result['score']))

        return analyzed_comments

    except Exception as e:
        logging.error(f"Failed to analyze comments: {e}")
        return []