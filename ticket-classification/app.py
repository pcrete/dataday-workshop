from flask import Flask,request
from src import utils

app = Flask(__name__)

@app.route("/predict",methods=['POST'])
def predict_category():
    text = request.json['text']
    prediction = utils.predict_class(text)
    return {'prediction': prediction}

if __name__=='__main__':
    app.run()
