from crewai_tools import tool
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)

@tool("YouTube Delete Comment Tool")
def delete_comment(comment_id: str, comment_text: str, youtube) -> None:
    """
    Deletes a YouTube comment if it contains any prohibited words from a specified CSV file.
    Parameters:
        comment_id (str): ID of the comment to be deleted.
        comment_text (str): Text content of the comment.
        youtube: Authenticated YouTube service object.
    """
    try:
        # Load prohibited words from a CSV file
        df = pd.read_csv('prohibited_words.csv')
        prohibited_words = df['words'].tolist()

        # Check if any prohibited word is found in the comment text
        if any(word.lower() in comment_text.lower() for word in prohibited_words):
            # Delete the comment if a prohibited word is found
            youtube.comments().setModerationStatus(
                id=comment_id,
                moderationStatus="deleted"
            ).execute()
            logging.info(f'Comment {comment_id} deleted due to containing prohibited words.')
        else:
            logging.info(f'No prohibited words found in comment {comment_id}.')

    except Exception as e:
        logging.error(f"Failed to delete comment {comment_id}: {e}")

# Example usage of the tool

def main():
    credentials_path = os.getenv('GOOGLE_CREDS_JSON_PATH')
    credentials = Credentials.from_authorized_user_file(credentials_path)
    youtube = build('youtube', 'v3', credentials=credentials)
    
    # Example comment data
    comment_id = 'YOUR_COMMENT_ID'
    comment_text = 'This is a sample comment to check.'

    delete_comment(comment_id, comment_text, youtube)

if __name__ == "__main__":
    main()