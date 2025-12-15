from flask import Flask, jsonify

app = Flask(__name__)     # 把“当前这个 Python 文件的位置”交给 Flask

@app.route("/")
def index():
    return "Hello CI 👋"

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
