import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature = 0.5
)

response = llm.invoke([{"role":"user","content":"Hello how are you"}])
print(response.content)

# print("Hi I am your AI assistant, how can I help you today?")
# while True:
#     user_input = input()
#     if user_input == "quit" or user_input == "exit" or user_input == "end":
#         print("Goodbye!")
#         break
#     print(f"Thanks for sharing {user_input}")