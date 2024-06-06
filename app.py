from flask import Flask

app = Flask(__name__)

@app.route('/backxlash')
def backxlash():
    return 'We Are BACKXLASH'

@app.route('/contact_us')
def contact_us():
    return 'CALL AT : 03034407897'

if __name__ == "__main__":
    app.run(debug=True)
