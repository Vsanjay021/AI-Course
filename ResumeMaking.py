import openai
import os
import webbrowser

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


personal_detail = """
name:sanjay v,
age:22,
place:bengaluru,
"""
education_qualification = """
Degree:B.E (Computer Science) 2018-2022
"""
prompt = f"""
Design a resume that takes some personal detail like 
{personal_detail}, and educational qualification like
{education_qualification} , add some skills from
the degree specific to that,and the format of the resume should be
<Personal detail>
<soft skills>-add some skills that is widely needed for companies 
<technial skills> - take this from the degeree qualifications
and the format should be in html
"""
response = get_completion(prompt)
with open('temp.html', 'w') as f:
    f.write(response)

# Open the HTML file in the default web browser
webbrowser.open('temp.html')
# display(HTML(response))
# print(response)
