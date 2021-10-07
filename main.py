from data import data
from flask import Flask,request,jsonify

app=Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "planet_data":data,
        "message":"sucessfull!"
    })
@app.route("/planet")
def planet():

    name=request.args.get("name")
    planet_data=next(item for item in data if item["name"]==name)
    return jsonify({
        "planet_data":planet_data,
        "message":"sucessfull!"
    })
if __name__ == "__main__":
    app.run(debug=True)
