from flask import Flask, request, jsonify
import openai 
from keys import API_KEY
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, World!!!'

@app.route('/chatbot', methods=["POST"])
def chatbot():
    print('test request',request)
    data = request.get_json()
    # prompt=(writeCoverLetterPrompt+data)
    whoAmI= "You are a friendly customer service chatbot. answer this question: "
    prompt= whoAmI+data
    openai.api_key = API_KEY
    response = openai.Completion.create(
        engine="text-davinci-001", #the AI model you choose to use
        temperature=1,# Level of creativity in the response
        prompt= prompt , #what you want to ask AI
        max_tokens=200, #Maximum tokens in the prompt AND response
        n=1, #The number of completions to generate
       # stop=None, # An optional setting to control response generation
        )
    print('!!',response.choices[0].text)
    print('response type !! ',type(response.choices[0].text))
    print('this is the chatbot response !!!',response.choices[0].text)
    data={'data':response.choices[0].text}
    return jsonify(data)


    
if __name__ == '__main__':
    app.run()
