import streamlit as st

st.set_page_config(page_title="My Streamlit App", layout="centered")

st.title("🚀 Streamlit on Railway")
st.write("Hello from your free deployed backend!")

name = st.text_input("What's your name?")
if name:
    st.success(f"Welcome, {name}! 🎉")
