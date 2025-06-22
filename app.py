import streamlit as st

st.set_page_config(page_title="🔧 Deployment Test", layout="wide")

st.title("🚀 Deployment Test App")
st.write("If you’re seeing this, your app is deploying properly!")

name = st.text_input("What's your name?")
if name:
    st.success(f"Welcome, {name} 👋 Your deployment is working!")
