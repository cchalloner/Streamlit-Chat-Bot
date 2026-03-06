
import streamlit as st
import random
import time

# Streamed response emulator
def response_generator():
    response = random.choice(
    [
    "Hello there! How can I assist you today?",
    "Hi, human! Is there anything I can help you with?",
    "I'm here and ready to help.",
    "Sure, I can help with that.",
    "Let me look into that for you.",
    "That's a great question.",
    "Here’s what I found.",
    "Give me a moment while I think about that.",
    "Absolutely! Let's work through it together.",
    "That depends on a few different factors.",
    "Thanks for asking!",
    "Let’s break that down.",
    "Here's a possible solution.",
    "I can help with that.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I tried to learn recursion… but I kept repeating myself.",
    "There are 10 types of people in the world: those who understand binary and those who don't.",
    "I would tell you a UDP joke, but you might not get it.",
    "Debugging: being the detective in a crime movie where you are also the murderer.",
    "Why did the computer show up at work late? It had a hard drive.",
    "I told my computer I needed a break, and it said: 'No problem — I’ll go to sleep.'",
    "Why do programmers hate nature? Too many bugs.",
    "Why did the developer go broke? Because they used up all their cache.",
    "Computers make very fast, very accurate mistakes.",
    "I would explain AI humor, but it's still in beta."
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

