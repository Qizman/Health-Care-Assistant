import openai
import json
import webScraper

def chat(user_input):
    #config json load
    with open('config.json') as f:
        try:
            config = json.load(f)
        except ValueError:
            print("File is empty")
            config = []
            exit()

    openai.api_key = config["openai"]['api_key']

    response = openai.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "Here is your medical knowledge: " + webScraper.get_Diseases()},
        {"role": "system", "content": "You are a health care assistant that when asked questions use previosly given context to help advise the Doctor?"},
        {"role": "user", "content": user_input},
    ])

    return response.choices[0].message.content