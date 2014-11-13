from flask import Flask
from flask import render_template
app = Flask(__name__)

# talks to index.html
@app.route("/")
def index():
    return render_template('index.html')

# allows it to run on local server
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8000,
        use_reloader=True,
        debug=True,
    )