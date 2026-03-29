import streamlit as st
import openai

openai.api_key = "PASTE_YOUR_API_KEY"

st.title("🚀 AI Job Assistant")

option = st.selectbox("Choose Tool", [
    "Resume Optimization",
    "Cover Letter",
    "HR Message",
    "SOP"
])

job_desc = st.text_area("Paste Job Description")
user_input = st.text_area("Paste Resume / Details")

def generate(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

if st.button("Generate"):
    if option == "Resume Optimization":
        prompt = f"Optimize resume based on job:\n{job_desc}\nResume:\n{user_input}"

    elif option == "Cover Letter":
        prompt = f"Write cover letter:\n{job_desc}\nUser:\n{user_input}"

    elif option == "HR Message":
        prompt = f"Write HR message:\n{job_desc}\nUser:\n{user_input}"

    elif option == "SOP":
        prompt = f"Write SOP:\n{user_input}"

    result = generate(prompt)
    st.write(result)
