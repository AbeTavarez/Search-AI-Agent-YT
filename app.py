import streamlit as st
from agent import call_agent


st.title("AI Agent")

with st.sidebar:
    st.header("Setting")
    
    
if query := st.chat_input("Ask me anything!"):
    st.chat_message("user").write(query)
    response = call_agent(query)
    st.chat_message("assistant").write(response)