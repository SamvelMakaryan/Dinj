from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for your app

# Define a route for the login page
@app.route('/login', methods=['POST'])
def login():
    # Get the JSON data from the request
    data = request.get_json()

    # Extract email and password from the JSON data
    email = data.get('email')
    password = data.get('password')

    # Check the email and password against a database or any authentication logic
    # For simplicity, we'll use hardcoded values here
    if email == 'user' and password == '123':
        # Successful login
        return jsonify({'success': True})
    else:
        # Login failed
        return jsonify({'success': False, 'error': 'Invalid email or password'})

@app.route('/sign-up', methods=['POST'])
def sign_up():
    # Get the JSON data from the request
    data = request.get_json()

    # Extract email and password from the JSON data
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    password2 = data.get('password2')

    # Check the email and password against a database or any authentication logic
    # For simplicity, we'll use hardcoded values here
    if email == 'user' and password == '123' and password2 == '123' and username == 'aaa':
        # Successful login
        return jsonify({'success': True})
    else:
        # Login failed
        return jsonify({'success': False, 'error': 'Invalid email or password'})


if __name__ == '__main__':
    app.run(debug=True)
