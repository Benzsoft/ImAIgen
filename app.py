from flask import Flask, render_template, request
import openai

from config import API_KEY




app = Flask(__name__)

openai.api_key = API_KEY

@app.route('/')
def index():
    return render_template('index.html')
import requests
import json
@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']

    # Call OpenAI API to generate images based on the prompt
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=50,
        n=3,  # Generate 3 images
        stop=None,
        temperature=0.7
    )

    generated_image_urls = [choice.text.strip() for choice in response.choices]

    return render_template('result.html', image_urls=generated_image_urls)
