import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

print("Hi I am your AI assistant, how can I help you today?")
while True:
    user_input = input()
    if user_input == "quit" or user_input == "exit" or user_input == "end":
        print("Goodbye!")
        break
    print(f"Thanks for sharing {user_input}")