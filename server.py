from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def home():
    return render_template('index.html')


@app.route('/sub', methods = ['GET'])
def process():
    return render_template('sub.html')

if __name__ == "__main__":
    app.run(debug=True)