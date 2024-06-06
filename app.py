from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def backxlash():
    return render_template('index.html', title='Welcome to My Flask App')

@app.route('/contact_us')
def contact_us():
    return 'CALL AT : 03034407897'

if __name__ == "__main__":
    app.run(debug=True)
