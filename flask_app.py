from flask import Flask, request, jsonify
from flask_cors import CORS

import BudgetApp
import PassWordGenerator

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()

    user_input = data['text']
    mode = data['app']

    if mode == 'budget':
        result = BudgetApp.user_input
    elif mode == 'password':
        result = PassWordGenerator.text
    else:
        result = 'Invalid Input'

    return jsonify({"response": result})



if __name__ == '__main__':
    app.run(debug=True)