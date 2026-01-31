import os
import gradio as gr
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

system_prompt="""
    You are a smart, confident ai assistant.
    You answer the user's questions in fun and unique ways.
"""

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature = 0.5
)

history=[]
prompt = ChatPromptTemplate.from_messages([("system", system_prompt),
                             MessagesPlaceholder("history"),
                             ("user", "{input}")])

chain = prompt | llm | StrOutputParser()

print("Hi I am your AI assistant, how can I help you today?")
page = gr.Blocks(title = "AI Assistant")

def chat(user_input, history):
    return "",[
        {'role':'user', 'content':'hello machine'},
    {'role':'assistant', 'content':'hello human'},
    ]
    # while True:
        # user_input = input()
        # response = chain.invoke({"input": user_input, "history": history})
        # history.append(HumanMessage(user_input))
        # history.append(AIMessage(response))
        # print(response)


with page:
    gr.Markdown(
        """
        # Chat with your AI assistant
        """
    )
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    msg.submit(chat,[msg, chatbot],[msg, chatbot])
    clear = gr.Button("Clear Chat")

page.launch(theme=gr.themes.Soft())


