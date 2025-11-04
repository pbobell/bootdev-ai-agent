import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys


def main():
    print("Hello from bootdev-ai-agent!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    prompt_length = len(sys.argv)

    if prompt_length == 1:
        print("no prompt provided")
        return 1
    
    messages = [types.Content(role="user", parts=[types.Part(text=str(sys.argv[1]))])]

    resp = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents= messages,
    )

    if "--verbose" in sys.argv:
        print(f"User prompt: {sys.argv[1]}")
        print(f"Prompt tokens: {resp.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {resp.usage_metadata.candidates_token_count}")

    print(resp.text)


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
