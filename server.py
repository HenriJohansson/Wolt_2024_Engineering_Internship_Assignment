from flask import Flask, request, jsonify
from src.controller import get_delivery_fee
from src.request import RequestVerification

app = Flask(__name__)

@app.route("/fee", methods=['POST'])
def fee():
    data = request.json
    try:
        verifier = RequestVerification(data)
    except:
        return jsonify(error_message)
    if verifier.isAcceptableFee() is not True:
        return jsonify(error_message)
    return jsonify({"delivery_fee": get_delivery_fee(data)})

error_message = {
        "error": 
            {
            "code": 400,
            "message": "Bad request",
            "details": "The request was invalid."
            }
        }

if __name__ == "__main__":
    app.run(debug=True)

