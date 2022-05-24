from random import choice
from flask import Flask, jsonify, render_template, url_for, request
from flask_cors import CORS
from werkzeug import exceptions
from models.bee import Bee

app = Flask(__name__)
CORS(app)

@app.route("/bees")
def list_bees():
    return jsonify({
        "success": True,
        "bees": Bee.get_all_as_dicts()
    })

@app.route("/bees/new", methods=["POST"])
def create_bees():
    try:
        data = request.json
        bee = Bee.create_bee(data["id"], data["name"], data["queen"])
        return jsonify({
            "success": True,
            "bee": bee.to_dict()
        }), 201
    except Exception as err:
        return jsonify({
            "success": False,
            "error": str(err)
        })

@app.route("/bees/<int:id>", methods=["GET", "DELETE"])
def interact_with_bee(id):

    try:
        bee = Bee.get_one_by_id(id)
        
        if request.method == "GET":
            return jsonify({
                "success": True,
                "bee": bee.to_dict()
            })
        
        elif request.method == "DELETE":
            bee.delete()
            return "", 204
    except Exception as err:
        return jsonify({
            "success": False,
            "error": str(err)
        })

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bee_list")
def display_bees_to_humans():
    bees = Bee.get_all_as_dicts()
    bees = sorted(bees, key=lambda x: x["queen"], reverse=True)
    return render_template("bee_list.html", bees=bees)

@app.errorhandler(exceptions.NotFound)
def page_not_found(err):
    return render_template("404.html", error=err)

if __name__ == "__main__":
    app.run(debug=True)