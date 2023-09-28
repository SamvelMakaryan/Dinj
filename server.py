from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Define a route for the login page
@app.route('/login', methods=['POST'])
def login():
    # Get the values of the email and password fields from the form
    email = request.form.get('email')
    password = request.form.get('password')

    # Check the email and password against a database or any authentication logic
    # For simplicity, we'll use hardcoded values here
    if email == 'user@example.com' and password == 'password123':
        # Successful login, redirect to a welcome page or perform other actions
        print("Access")
        return redirect(url_for('welcome'))
    else:
        # Login failed, you can display an error message or redirect to the login page
        print("Failed")
        return render_template('login.html', error='Invalid email or password')

# Define a route for the welcome page (you can create this HTML page)
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)

