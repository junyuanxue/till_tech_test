import os
from flask import Flask, render_template, json, request, redirect, url_for, session
from order import Order

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route("/")
def index():
    order = Order(load_menu())
    session["order"] = "hello"
    return render_template("index.html")

@app.route("/items", methods=["POST"])
def add_item():
    item = request.form.get("item")
    order.add_item(item)
    return redirect(url_for("index"))


def load_menu():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.abspath(SITE_ROOT + "/../hipstercoffee.json")
    return json.load(open(json_url))


if __name__ == "__main__":
    app.run()
