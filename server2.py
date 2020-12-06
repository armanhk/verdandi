from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'multiply 5 80'

app.run(port=9675)