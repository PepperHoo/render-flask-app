from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    secret = os.getenv("SECRET_MESSAGE", "No Environment Variable Found")
    return render_template("index.html", secret=secret)

if __name__ == '__main__':
    app.run(debug=True)