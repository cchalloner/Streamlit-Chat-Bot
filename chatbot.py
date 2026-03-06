
import streamlit as st
import random
import time

# Streamed response emulator
def response_generator():
    response = random.choice(
    [
    "Hello there! How can I assist you today?",
    "Hi, human! Is there anything I can help you with?",
    "Do you need help?",
    "Greetings! What can I help you with today?",
    "I'm here and ready to help.",
    "Sure, I can help with that.",
    "Let me look into that for you.",
    "That's a great question.",
    "I think I can help you with that.",
    "Here’s what I found.",
    "Give me a moment while I think about that.",
    "Absolutely! Let's work through it together.",
    "I'm not completely sure, but here's my best guess.",
    "That depends on a few different factors.",
    "Thanks for asking!",
    "Interesting question!",
    "Let me explain.",
    "Here's a possible solution.",
    "I can help with that.",
    "That's something I can definitely assist with.",
    "Let’s break that down.",
    "Good question!",
    "Here’s what I recommend.",
    "That makes sense.",
    "I'm glad you asked."
    ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What's up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write_stream(response_generator())

# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})

