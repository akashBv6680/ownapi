from fastapi import FastAPI
from pydantic import BaseModel
from ai_agent import MyAIAgent

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/chat")
def chat(input_text: InputText):
    agent = MyAIAgent()
    response = agent.respond(input_text.text)
    return {"response": response}
