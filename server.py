from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'add 194 4444'

app.run(port=1337)