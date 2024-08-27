from flask import Flask, render_template

app = Flask("Website")


@app.route("/")
def home():
    return render_template("Home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temp = 16
    return {
    "station": station,
    "date": date,
    "temp": temp
    }


app.run(debug=True, port=5001)