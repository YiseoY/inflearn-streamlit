import streamlit as st
from dotenv import load_dotenv
from llm import get_ai_response
load_dotenv() 

st.set_page_config(page_title="개인정보보호법 챗봇", page_icon="🤖")

st.title("개인정보보호법 챗봇 🤖")
st.caption("개인정보보호법에 대한 질문을 해보세요!")


if 'message_list' not in st.session_state:
    st.session_state.message_list = []

print(f"before == {st.session_state.message_list}")
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_question := st.chat_input(placeholder="개인정보보호법에 대해 궁금한 점을 입력하세요..."):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner("AI가 답변을 생성하는 중입니다..."):
        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"):
            ai_message = st.write_stream(ai_response)
            st.session_state.message_list.append({"role": "ai", "content": ai_message})



