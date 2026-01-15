import streamlit as st
from src.brain.flow import create_drafting_graph

st.set_page_config(page_title="Agentic Drafter", page_icon="✍️")

st.title("🚀 Drafting Agent v1.0")
st.markdown("---")

# Sidebar for configuration
with st.sidebar:
    st.header("Settings")
    mode = st.selectbox("Drafting Mode", ["Creative", "Technical", "Academic"])
    st.info("Using Gemini 1.5 Flash (Free Tier)")

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("What should I draft today?")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Run the Agentic Flow
    with st.spinner("Agents are collaborating..."):
        app = create_drafting_graph()
        result = app.invoke({"task": user_input, "revision_number": 0})
        
        # Display the result
        with st.chat_message("assistant"):
            st.markdown(result["draft"])
            st.download_button("Download Draft", result["draft"], file_name="draft.md")