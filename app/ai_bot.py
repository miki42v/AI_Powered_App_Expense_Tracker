# app/ai_bot.py
import os
from openai import OpenAI
from dotenv import load_dotenv

class AIBot:
    """
    A class to interact with the NVIDIA API using an OpenAI-compatible client.
    """
    def __init__(self):
        """
        Initializes the AIBot and sets up the client to point to NVIDIA's API.
        """
        load_dotenv()
        self.api_key = os.getenv("NVIDIA_API_KEY")
        if not self.api_key:
            raise ValueError("NVIDIA_API_KEY not found in environment variables.")

        # This is the key part: initializing the OpenAI client with NVIDIA's details
        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=self.api_key
        )

    def get_answer(self, question: str) -> str:
        """
        Gets an answer from the NVIDIA API for a given question.
        """
        try:
            completion = self.client.chat.completions.create(
                model="meta/llama3-8b-instruct",  # Using a recommended model
                messages=[
                    {"role": "system", "content": "You are a helpful and friendly assistant."},
                    {"role": "user", "content": question}
                ],
                temperature=0.5,
                top_p=1,
                max_tokens=1024,
                # We use stream=False to get the whole answer at once, which is simpler for this app
                stream=False  
            )
            
            # The response structure is the same as OpenAI's, so this code is familiar
            answer = completion.choices[0].message.content
            return answer.strip()

        except Exception as e:
            # Provide a more detailed error message if something goes wrong
            return f"An error occurred with the API call: {e}"