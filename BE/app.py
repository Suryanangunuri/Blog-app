from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database of users (for demonstration purposes)
users_db = {
    "test@example.com": {"password": "test1234"},
    "user@domain.com": {"password": "password123"},
    "1234567890": {"password": "phonepassword123"}
}

# Helper function to validate credentials
def validate_user(identifier, password):
    # Check if identifier (email/phone number) exists in the database
    if identifier in users_db:
        # Check if the provided password matches the stored password
        if users_db[identifier]["password"] == password:
            return True
    return False

@app.route('/login', methods=['POST'])
def login():
    # Get user input from request
    data = request.get_json()

    identifier = data.get('identifier')  # email or phone number
    password = data.get('password')

    if not identifier or not password:
        return jsonify({"message": "Please provide both identifier (email/phone) and password."}), 400

    # Validate the user credentials
    if validate_user(identifier, password):
        return jsonify({"result": True, "message": "Login successful!"}), 200
    else:
        return jsonify({"result": False, "message": "Invalid credentials."}), 401

if __name__ == '__main__':
    app.run(debug=True)
