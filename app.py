from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return "Image server is running"

@app.route("/images/<path:filename>")
def images(filename):
    return send_from_directory("public/images", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
