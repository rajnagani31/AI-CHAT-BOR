# from openai import OpenAI
from dotenv import load_dotenv
# import os
from system_prompt import SYSTEM_PROMPT
from google import genai
from google.genai.types import GenerateContentConfig, HttpOptions
# from chat_bot import query

load_dotenv()
client = genai.Client(http_options=HttpOptions(api_version="v1"))

# api_key=st.secrets["GEMINI_API_KEY"]
# api_key=str(GEMINI_API_KEY)
# client=OpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )
# client=OpenAI()
# openai.api_key = os.environ['OPENAI_API_KEY']
data=SYSTEM_PROMPT
# ans=[]
def bot_call(query):

        # print("query",query)


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        # system_instruction = SYSTEM_PROMPT,
        contents=query,
        config=GenerateContentConfig(
        system_instruction=[
            data
        ]
    ),

    )

    msg=response.text
    print("MSG",msg)
        # ans.append({'role':'assistant','content':msg})
    # return ({'role':'assistant','content':msg})
    return msg

# bot_call("What is your name")  # Example call to test the function