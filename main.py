import openai 
from api_secrets import API_KEY

openai.api_key = API_KEY

prompt = "how many days are in a year"

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=6)

print(response.choices[0].text)