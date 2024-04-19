from crewai_tools import tool
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os
import logging

logging.basicConfig(level=logging.INFO)

@tool("YouTube Report Comment Tool")
def report_comment(comment_id: str) -> None:
    """
    Flags a YouTube comment for review by platform moderators or bans the author.
    Parameters:
        comment_id (str): ID of the comment to report.
    """
    try:
        credentials_path = os.getenv('GOOGLE_CREDS_JSON_PATH')
        credentials = Credentials.from_authorized_user_file(credentials_path)
        youtube = build('youtube', 'v3', credentials=credentials)
        
        youtube.comments().setModerationStatus(
            id=comment_id,
            moderationStatus="published",
            banAuthor=True
        ).execute()
        logging.info(f'Reported comment {comment_id} and banned author.')

    except Exception as e:
        logging.error(f"Failed to report comment {comment_id}: {e}")