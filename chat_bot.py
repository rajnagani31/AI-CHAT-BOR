# from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
# from google import generativeai
import os
from system_prompt import SYSTEM_PROMPT
from bot import bot_call
load_dotenv()
# api_key=st.secrets["GEMINI_API_KEY"]
# client=OpenAI(
#     api_key=api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )
# client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# openai.api_key = os.environ['OPENAI_API_KEY']
# if "OPENAI_API_KEY" not in st.secrets:
#     st.error("❌ OPENAI_API_KEY not found in secrets!")
# else:
#     st.success("✅ API key loaded!")
with st.sidebar:
    with st.expander("Information abot chat bot"):
        st.write("""
        1.Give all answers the question\n
        2.Give answer in Both Language English and Hindi(hinglish)\n
        3.Chat bot Train for solve profassional life problem
      """)

    st.title("Bot Source code")
    "[![Open in GitHub ](https://github.com/codespaces/badge.svg)](https://github.com/rajnagani31/Ai-chat-bot)"

st.title("💬Chat Bot:Solw your Problum")
query=st.chat_input("🚀 Enter your any Question")


# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])
SYSTEM_PROMPT=SYSTEM_PROMPT
# massages=[]
if not query:
    st.subheader("🚀 Ask any Problum")

if query:
    st.subheader(f"🚀{query}")
    # print("query",query)
    if not query:
        st.info("Plese write your question")
    msg=bot_call(query)   
    st.chat_message("assistant").write(msg) 
    # response=client.chat.completions.create(
    #     # model="gemini-2.5-flash",
    #     model='gpt-4.1-nano',
    #     messages=[
    #          {'role':'system','content':SYSTEM_PROMPT},
    #          {'role':'user','content':query}
    #          ]
    # )

    # msg=response.choices[0].message.content
    # massages.append({'role':'assistant','content':msg})

    
        # Show chat history
    # for msg in st.session_state.messages[1:]:  # Skip system message
    #         # st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")
    #         st.chat_message(msg["role"]).write(msg["content"])
