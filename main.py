import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set. Please check your .env file.")

def test_connection():
    # Initialize the official Google Gen AI Client
    client = genai.Client(api_key=api_key)
    
    print("Connecting to Gemini API...")
    
    # We use gemini-2.5-flash for speed and generous free-tier limits
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Say 'Hello! Forge is ready.' and give one short tip for building an AI agent."
    )
    
    print("\n--- Model Response ---")
    print(response.text)
    print("----------------------\n")

if __name__ == "__main__":
    test_connection()
