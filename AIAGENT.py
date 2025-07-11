import streamlit as st
import requests

st.title("My Chatbot")

input_text = st.text_input("You: ")
if input_text:
    response = requests.post("https://my-api.com/chat", json={"text": input_text})
    st.write("Bot:", response.json()["response"])
