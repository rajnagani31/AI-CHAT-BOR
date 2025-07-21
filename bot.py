from openai import OpenAI
from dotenv import load_dotenv
import os
from system_prompt import SYSTEM_PROMPT
# from chat_bot import query

load_dotenv()
# api_key=st.secrets["GEMINI_API_KEY"]
# api_key=str(GEMINI_API_KEY)
client=OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
# client=OpenAI()
# openai.api_key = os.environ['OPENAI_API_KEY']
SYSTEM_PROMPT=SYSTEM_PROMPT
# ans=[]
def bot_call(query):

        # print("query",query)
        response=client.chat.completions.create(
            model="gemini-1.5-flash",
            # model='gpt-4.1-nano',
            messages=[
                {'role':'system','content':SYSTEM_PROMPT},
                {'role':'user','content':query}
                # {'role':'user','content':'hi'}

                ]
        )

        msg=response.choices[0].message.content
        # print("MSG",msg)
        # ans.append({'role':'assistant','content':msg})
    # return ({'role':'assistant','content':msg})
        return msg

