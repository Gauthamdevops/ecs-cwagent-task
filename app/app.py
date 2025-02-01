import os
import logging
from flask import Flask, render_template, request


log_dir = '/var/log/my-app-log'

log_file = os.path.join(log_dir, 'my-app-log.log')

# Check if the directory exists, if not, create it
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# Test log
logging.info("Flask app has started!")
logger = logging.getLogger()

app = Flask(__name__)

# Hardcoded password for simplicity (this can be replaced with more secure methods)
correct_password = "password123"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve the name and password from the form
        name = request.form['name']
        password = request.form['password']
        
        # Validate the password
        if password == correct_password:
            return render_template('greetings.html', name=name)
        else:
            return render_template('login.html', error="Invalid password, please try again.")
    
    return render_template('login.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
