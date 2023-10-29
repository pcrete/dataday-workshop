from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    data = {
        'text': "Hello "+request.args.get('text'),
        'category': request.args.get('category'),
    }
    return jsonify(data)


@app.route('/calculate', methods=['POST'])
def calculate():
    # your function here..
    return jsonify({})


@app.route('/home', methods=['GET'])
def myhome():
    text = request.args.get('text')
    return f"""
<div style="text-align: center">
    <h1>Hello World! </h1>
    <h2>{text} </h2>
</div>
"""

if __name__ == '__main__':
    app.run(debug=True)
