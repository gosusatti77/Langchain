from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

#prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please answer the question."),
        ("human", "{input}"),
    ]
)

#streamlit app

st.title("LangChain Chatbot")
st.write("This is a LangChain chatbot using OpenAI's GPT-3.5-turbo model.")
st.write("Ask me anything!")
input_text = st.text_input("Search the topic you want to know about:")

#openai model
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
output_parser = StrOutputParser()
llm_chain = prompt | model | output_parser

if input_text:
    st.write(llm_chain.invoke({"input": input_text}))
