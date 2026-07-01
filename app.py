import streamlit as st
import requests

# create the title for the page
st.title("🤝 Your Personal Assistant")

# add subheader
st.subheader("What can your personal assistant do?")

# create a list of what your assistant can do
st.markdown("""
            1. Answer questions on various topics.   
            2. Arrange Calendar events and meetings.  
            3. Read your emails and send replies, can even summarize them for you.
            4. Manage your tasks and to-do lists.
            5. Take quick notes for you.
            6. Track your expenses and budgeting.
            """)

# add chats subheader
st.subheader("💬 Chat with your assistant")

# create a session state for message history and session ID
if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_id" not in st.session_state:
    import uuid
    st.session_state.session_id = str(uuid.uuid4())

# show the messages in chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# create a chat input box
user_message = st.chat_input()

      
# if user sends a message
if user_message:
    with st.chat_message("user"):
        st.markdown(user_message)
        # append the user message to message history
        st.session_state.messages.append({"role": "user", "content": user_message})
    
    # send the user message to the n8n webhook with the sessionId
    response = requests.post(
        "https://escalator-conducive-valuables.ngrok-free.dev/webhook/f0b8ff40-f872-4c8f-9a68-7564b6ac342c",  # replace with your n8n webhook URL
        json={
            "message": user_message,
            "sessionId": st.session_state.session_id
        }
    )
    
    # get the AI response from webhook
    try:
        response_json = response.json()
        if isinstance(response_json, list) and len(response_json) > 0:
            ai_response = response_json[0].get("output", str(response_json))
        elif isinstance(response_json, dict):
            ai_response = response_json.get("output", response_json.get("message", str(response_json)))
        else:
            ai_response = str(response_json)
    except Exception as e:
        ai_response = f"Failed to parse response: {e}"
    
    # display the AI response in chat
    with st.chat_message("assistant"):
        st.markdown(ai_response)
        # append the AI response to message history
        st.session_state.messages.append({"role": "assistant", "content": ai_response})