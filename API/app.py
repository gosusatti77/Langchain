from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Langchain Server",
    description="API for LangServe with FastAPI",
    version="0.1.0",
)

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
model_ollama = OllamaLLM(model="mistral")


add_routes(app, model, path="/openai")

prompt1 = ChatPromptTemplate.from_template(
    "write an essay about {input} in 100 words."
)

prompt2 = ChatPromptTemplate.from_template(
    "write a poem about {input} in 100 words."
)

add_routes(
    app,
    prompt1 | model,
    path="/essay"
)

add_routes(
    app,
    prompt2 | model_ollama,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app,host="localhost", port=8000)