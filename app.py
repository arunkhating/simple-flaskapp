from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is running in a container! \
    This is for Testing the Flask Container \
    "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
