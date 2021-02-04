from flask import Flask
from flask import jsonify, render_template
from utils.map import get_map


import random
import os

app = Flask(__name__)



data = []


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")



@app.route("/route")
def analyse():
    start_location = (50.454096, 3.9418326)
    end_location = (50.4537353, -3.9451452)

    data = get_map(start_location, end_location)

    return render_template("route.html", data=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
