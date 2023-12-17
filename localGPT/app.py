from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import AzureOpenAI

import time
import json
import httpx
import openai

client = AzureOpenAI(
    azure_endpoint="https://od232800-openai-dev.openai.azure.com/", 
    api_version="2023-07-01-preview", 
    api_key="540bb4c429584c4e866e481c6b4b2637",
)
 
app = Flask(__name__)
CORS(app) 

@app.route('/api/chat', methods=['POST'])
def chat():
    message = request.json['message']
    response = client.chat.completions.create(
        model="firstcontact",
        messages=[
            {"role": "user", "content": message},
            {"role": "system", "content": "Ask for clarification if needed."}],
        # functions = functions,
        # function_call="auto",
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)
    return jsonify({"message": response.choices[0].message.content})
 
# from urllib.request import urlopen
# @app.route('/api/images', methods=['POST'])

# def image():
#     message = request.json['message']
#     image = client.images.generate(prompt=message)
#     return urlopen(image.data[0].url).read()
#     # return jsonify({"message": image.data[0].url})

if __name__ == '__main__':
    app.run(debug=True)
