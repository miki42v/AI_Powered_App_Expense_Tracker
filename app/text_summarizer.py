# app/text_summarizer.py
import os
import requests
from dotenv import load_dotenv
import time

class TextSummarizer:
    """
    A class to summarize text using the Hugging Face Inference API.
    """
    def __init__(self):
        """
        Initializes the TextSummarizer and sets up the Hugging Face API token.
        """
        load_dotenv()
        self.api_token = os.getenv("HUGGINGFACE_API_TOKEN")
        if not self.api_token:
            raise ValueError("HUGGINGFACE_API_TOKEN not found in environment variables.")
        
        # We will use a popular and reliable model for summarization
        self.api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        self.headers = {"Authorization": f"Bearer {self.api_token}"}

    def _query_api(self, payload):
        """
        Private method to send a request to the Hugging Face API.
        """
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        return response.json()

    def summarize(self, text: str) -> str:
        """
        Summarizes the given text.
        Note: The 'sentences' parameter is no longer used as the model decides the length.
        """
        try:
            # Hugging Face models can sometimes take a moment to "wake up" if they aren't
            # being used frequently. We will handle this by retrying.
            output = self._query_api({
                "inputs": text,
                "parameters": {"min_length": 30, "max_length": 150} # You can adjust these values
            })

            # Check for the initial model loading error
            if "error" in output and "is currently loading" in output["error"]:
                wait_time = output.get("estimated_time", 10)
                st.info(f"Model is loading, please wait about {int(wait_time)} seconds...")
                time.sleep(wait_time)
                # Retry the query after waiting
                output = self._query_api({"inputs": text})

            # Check for other errors
            if "error" in output:
                 return f"An API error occurred: {output['error']}"

            # Successfully get the summary
            summary = output[0]['summary_text']
            return summary.strip()

        except Exception as e:
            return f"An unexpected error occurred: {e}"