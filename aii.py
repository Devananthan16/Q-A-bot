import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🚀 Simple AI App with Streamlit + OpenAI")


user_input = st.text_input("Ask me anything:")

if user_input:
    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ],
    )

    st.subheader("AI Response:")
    st.write(response.choices[0].message.content)


# I was learnig a data science course from guvi and 
# i took a reference from my mentor's notebook and 
# i refered a documentotion from openai and streamlit to create this app. 
# https://platform.openai.com/docs/api-reference/chat