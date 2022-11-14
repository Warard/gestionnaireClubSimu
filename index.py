from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/")
def Index():
    return render_template("index.html")

@app.route("/inscription")
def inscription():
    return render_template("inscription.html")

@app.route("/reservation")
def reservation():
    return render_template("reservation.html")

@app.route("/calendrier")
def calendrier():
    return render_template("calendrier.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")
if __name__ == "__main__":
    app.run(debug=True)