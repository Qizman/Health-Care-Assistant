import openai
import json

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
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a Doctors assistant that when asked questions use previosly given context to help advise the docctor?"},
    {"role": "user", "content": "what is the best treatment for a cold?"}
  ]
)

print(response.choices[0].message.content)