from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD working successfully 🚀"

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8081)
