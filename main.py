from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("main.html")

@app.route('/importance-of-independence-day-deepti')
def deeptione():
    return render_template("importance-of-independence-day-deepti.html")

@app.route('/freedom-and-responsibility-sadana')
def sadana():
    return render_template("freedom-and-responsibility-sadana.html")

@app.route('/history-of-independence-haripriya')
def haripriya():
    return render_template("history-of-independence-haripriya.html")

@app.route('/unsung-freedom-fighters-hrithik')
def hrithik():
    return render_template("unsung-freedom-fighters-hrithik.html")

@app.route('/famous-freedom-fighters-raghavi')
def raghavi():
    return render_template("famous-freedom-fighters-raghavi.html")

@app.route('/indian-flag-deepti')
def deeptitwo():
    return render_template("indian-flag-deepti.html")



if __name__ == '__main__':
    app.run(debug=True)
