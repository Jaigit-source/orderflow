from flask import Flask, jsonify, request
import os

app = Flask(__name__)
ENV = os.getenv("APP_ENV", "dev")
DB_PASS = os.getenv("DB_PASSWORD", "none")
NEW_CHECKOUT = os.getenv("NEW_CHECKOUT", "false")

@app.route('/health')
def health():
    return jsonify({"status": "UP", "env": ENV})

@app.route('/order', methods=['POST'])
def order():
    data = request.get_json()
    return jsonify({"orderId": data.get("orderId"), "status": "PROCESSED"})

@app.route('/checkout', methods=['POST'])
def checkout():
    if NEW_CHECKOUT == "true":
        return jsonify({"message": "new checkout flow"})
    return jsonify({"message": "legacy checkout flow"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
