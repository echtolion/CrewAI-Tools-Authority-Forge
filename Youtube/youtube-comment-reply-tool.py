from crewai_tools import tool
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os
import logging

logging.basicConfig(level=logging.INFO)

@tool("YouTube Auto-Reply Tool")
def reply_to_comment(comment_id: str, response_text: str) -> None:
    """
    Automatically replies to a YouTube comment based on predefined rules.
    Parameters:
        comment_id (str): ID of the comment to reply to.
        response_text (str): Text of the reply.
    """
    try:
        credentials_path = os.getenv('GOOGLE_CREDS_JSON_PATH')
        credentials = Credentials.from_authorized_user_file(credentials_path)
        youtube = build('youtube', 'v3', credentials=credentials)
        
        response = youtube.comments().insert(
            part="snippet",
            body={"snippet": {"parentId": comment_id, "textOriginal": response_text}}
        ).execute()
        logging.info(f'Replied to comment {comment_id} successfully.')

    except Exception as e:
        logging.error(f"Failed to reply to comment {comment_id}: {e}")