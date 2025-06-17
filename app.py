import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyA8Sky74XPjGgqfH2KJjInqKJ6ugx7IUtE")  
model = genai.GenerativeModel("gemini-1.5-flash")

st.title(" Sentiment Analyzer")

# Text input
user_input = st.text_area("Enter your text here:")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing with Gemini 1.5 Pro..."):
            prompt = f"""Analyze the sentiment of the following text. 
Reply with only one word: Positive, Negative, or Neutral.

Text: {user_input}
Sentiment:"""
            try:
                response = model.generate_content(prompt)
                sentiment = response.text.strip()
                st.success(f"Sentiment: *{sentiment}*")
            except Exception as e:
                st.error(f"Error: {str(e)}")