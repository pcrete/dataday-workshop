import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

HOST = os.getenv('HOST', 'http://localhost:5001')
# HOST = 'https://tagger-api-t23b23wjiq-uc.a.run.app'

@app.route('/', methods=['GET'])
def index():
    data = {
        "text": request.args.get('text')
    }
    return render_template('demo.html', data=data)


@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('content')
    payload = {'text': text}
    response = requests.post(HOST+'/predict', json=payload)

    prediction = {
        'output': response.json().get('prediction')
    }

    return render_template('demo.html', prediction=prediction, text=text)


if __name__ == "__main__":
    app.run()