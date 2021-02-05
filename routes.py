from flask import Flask
from flask import jsonify, render_template
from utils.map import get_map
from utils.other_way import demo_map1
from utils.second_way import demo_map2


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
    # TODO : request var from GET/POST 
    start_location = (50.454096, 3.9418326)
    end_location = (50.4537353, -3.9451452)

    data = get_map(start_location, end_location)

    return render_template("route.html", data=data)

@app.route("/route1")
def demo1():
    data = demo_map1()
    return render_template("route.html", data=data)

@app.route("/route2")
def demo2():
    data = demo_map2()
    return render_template("route.html", data=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
