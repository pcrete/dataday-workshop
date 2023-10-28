from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_dimension(ratio, value):
    width, height = map(int, ratio.split(':'))
    if width == 0 or height == 0:
        return 0
    return int(value * height / width)

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'GET':
        ratio = request.args.get('ratio')
        value = request.args.get('value')
    elif request.method == 'POST':
        data = request.json
        ratio = data.get('ratio')
        value = data.get('value')
    else:
        return jsonify({"error": "Invalid request method"})

    if not ratio or not value:
        return jsonify({"error": "Both 'ratio' and 'value' must be provided as integers."})

    try:
        value = int(value)
        ratio = str(ratio)
        result = calculate_dimension(ratio, value)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input. 'value' must be an integer."})

if __name__ == '__main__':
    app.run(debug=True)
