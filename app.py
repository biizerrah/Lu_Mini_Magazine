from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/bazar")
def bazar():
    return render_template("bazar.html")

@app.route("/sequilhos")
def sequilhos():
    return render_template("sequilhos.html")

if __name__ == 'main':
    app.run(debug=True)