from flask import Flask, jsonify

app = Flask(__name__)

# Переменная, которую будет получать ESP32-C3 Mini
variable_value = "Nastia LOX"

@app.route("/get_variable", methods=["GET"])
def get_variable():
    return jsonify({"value": variable_value})

if __name__ == "__main__":
    app.run(host="192.168.204.26", port=5000, debug=False)
