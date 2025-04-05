import requests
import streamlit as st

def get_response_from_api(input_text):
    data={'input': {"input": input_text}}
    response=requests.post("http://localhost:8000/essay/invoke",json=data)
    response_data = response.json()
    return response_data["output"]["content"]
    # try:
    #     response_data = response.json()
    #     if "output" in response_data:
    #         return response_data["output"]["content"]
    #     else:
    #         return f"Error: 'output' key missing. Full response: {response_data}"
    # except requests.exceptions.JSONDecodeError:
    #     return f"Error: Unable to parse JSON. Raw response: {response.text}"
    
def get_response_from_ollama(input_text_ollama):
    data={'input':{"input":input_text_ollama}}
    response=requests.post("http://localhost:8000/poem/invoke",json=data)
    response_data = response.json()
    return response_data["output"]
    # return response.json()['output']["content"]

st.title("LangChain API Client")
st.write("This is a LangChain API client using FastAPI.")
input_text = st.text_input("Write an essay about:")
input_text_ollama = st.text_input("write a poem about:")

if input_text:
    response = get_response_from_api(input_text)
    st.write(response)

if input_text_ollama:
    response_ollama = get_response_from_ollama(input_text_ollama)
    st.write(response_ollama)