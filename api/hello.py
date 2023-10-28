from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    data = {
        'text': "Hello "+request.args.get('text'),
        'category': request.args.get('category'),
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
