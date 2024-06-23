import streamlit as st
from catalog_agent_setup import get_response

# Heading
st.title("Product Catalog Dataset Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if user_input := st.chat_input("Enter your query about the dataset:"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_input)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Process user input with LangChain agent
    with st.chat_message("assistant"):
        st.markdown("Processing...")

        # Get the response from the agent
        response = get_response(user_input)

        # Display assistant response in chat message container
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
