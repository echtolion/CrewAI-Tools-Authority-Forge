from crewai_tools import tool
import requests
import logging
from llmware.models import ModelCatalog
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
logging.basicConfig(level=logging.INFO)

@tool("Facebook Page Comment Sentiment Analysis and Reply Tool")
def analyze_and_reply_facebook_comments(pages_file: str) -> None:
    """
    Processes multiple Facebook Pages from a CSV file to analyze comments by specified users and replies accordingly.
    The CSV file should have columns: pages, user_id.
    Parameters:
        pages_file (str): Path to the CSV file containing Facebook Page IDs and User IDs.
    """
    try:
        # Load page ids, and user ids from CSV
        df = pd.read_csv(pages_file)
        
        # Access token from environment variable
        access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
        if not access_token:
            raise ValueError("Facebook access token not found in environment variables.")

        # Initialize the LLMware sentiment analysis model
        sentiment_tool = ModelCatalog().tool_test_run("slim-sentiment-tool")
        
        # Iterate through each row in the dataframe
        for index, row in df.iterrows():
            page_id = row['pages']
            user_id = row['user_id']

            # Fetch comments from the Facebook page
            base_url = f"https://graph.facebook.com/v12.0/{page_id}/feed"
            params = {
                'fields': 'comments{from,message}',
                'access_token': access_token
            }
            response = requests.get(base_url, params=params)
            data = response.json()

            # Analyze and respond to comments
            for post in data.get('data', []):
                if 'comments' in post:
                    for comment in post['comments']['data']:
                        if comment['from']['id'] == user_id:
                            sentiment_result = sentiment_tool.analyze_text(comment['message'])
                            if sentiment_result['score'] < 0:
                                reply_message = "We are sorry to hear you feel this way. How can we assist you further?"
                            else:
                                reply_message = "Thank you for your positive feedback!"

                            # Post a reply to the comment
                            reply_url = f"https://graph.facebook.com/{comment['id']}/comments"
                            reply_params = {
                                'message': reply_message,
                                'access_token': access_token
                            }
                            requests.post(reply_url, params=reply_params)
                            logging.info(f"Replied to comment {comment['id']} successfully.")

    except Exception as e:
        logging.error(f"Failed to process pages: {e}")

# Example usage of the tool
def main():
    pages_file = 'path_to_your_csv_file.csv'
    analyze_and_reply_facebook_comments(pages_file)

if __name__ == "__main__":
    main()