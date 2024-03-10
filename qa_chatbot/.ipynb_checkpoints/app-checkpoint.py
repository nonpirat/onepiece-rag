import streamlit as st

if "messages" not in st.session_state.keys():
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]
if "messages" in st.session_state.keys():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

user_prompt = st.chat_input()

if user_prompt is not None:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

if st.session_state.messages[-1]["role"] == "user":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            response = "Text generation"
            st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})


