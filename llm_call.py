
'''to load the env variables where we store the api keys to ai models'''
from dotenv import load_dotenv
load_dotenv(override=True);

'''setting up api_keys'''
import os
openai_api_key= os.getenv("OPENAI_API_KEY");
from openai import OpenAI;
openai = OpenAI();

'''will ask the AI to pick up a business area in finance for potential agentic ai solution'''

messages = [{"role": "user", "content": "Pick a business area in finance that has the potential for agentic AI solution"}]
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

business_idea = response.choices[0].message.content
display(Markdown(business_idea))

print(response.choices[0].message.content)


'''Asking to identify one specific pain point in this area and give us the details about it'''

messages=[{"role":"user","content":"Highlight in detail one pain point in Investment Management and Portfolio Optimization business area. Please keep the ouput in not more than 1000 words"}]
response=openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

pain_point = response.choices[0].message.content
display(Markdown(pain_point))


'''Asking AI to propose a solution to this pain point '''
messages=[{"role":"user", "content":"Please propose an agentic ai solution for Data Integration and Quality issues in  Investment Management and Portfolio Optimization business area."}]
response= openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

agenticAI_solution = response.choices[0].message.content
display(Markdown(agenticAI_solution))
