from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'divide 2 9675'

app.run(port=4444)