from flask import Flask,request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/mm", methods=["GET"])
def mm():
       return jsonify({"message": "User deleted!"})

if __name__ == "__main__":
    app.run(debug=True)