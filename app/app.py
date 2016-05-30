import os
from flask import Flask, render_template, json, request
from order import Order

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/items", methods=["POST"])
def add_item():
    print("before json url")
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "hipstercoffee.json")
    print("after json url")
    menu = json.loads(open(json_url))
    print(menu)

    item = request.form.get("item")
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
