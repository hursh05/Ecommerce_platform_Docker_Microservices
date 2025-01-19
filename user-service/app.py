from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    return jsonify({"message": f"User {data['name']} created successfully!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
