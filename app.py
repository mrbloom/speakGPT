# app.py
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    response = openai.Completion.create(engine="text-davinci-003", prompt=user_message, max_tokens=150)
    message = response.choices[0].text.strip()
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)
