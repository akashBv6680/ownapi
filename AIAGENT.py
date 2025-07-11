import streamlit as st
import requests

st.title("My Chatbot")

api_url = "https://api.together.xyz/v1/chat/completions"

api_key = "tgp_v1_BvPlhwF-WQfAOBUmnV8OLm37Sdzbqmp9Uu8faPNSeIA"

input_text = st.text_input("You: ")
if input_text:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [{"role": "user", "content": input_text}],
        "max_tokens": 512,
        "temperature": 0
    }
    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 200:
        try:
            response_json = response.json()
            st.write("Bot:", response_json["choices"][0]["message"]["content"])
        except (KeyError, requests.exceptions.JSONDecodeError) as e:
            st.write("Bot: An error occurred while processing the response.")
            st.write("Error:", str(e))
            st.write("Response:", response.text)
    else:
        st.write("Bot: An error occurred while making the request.")
        st.write("Status Code:", response.status_code)
        st.write("Response:", response.text)
