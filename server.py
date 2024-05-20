from flask import Flask, Response, jsonify
from flask_cors import CORS
import crawler

app = Flask(__name__)
CORS(app) #, origins=['http://localhost:5173', 'http://127.0.0.1:5173'])  # Initialize CORS for the entire app

@app.route("/")
def hello_world():
    return "<h1>Welcome to Getting-to-Philosophy</h1><a href='/stream/'>Stream</a>"

@app.route("/health")
def health():
    print("aw awurade")
    return jsonify({"status": "OK"})

@app.route('/stream')
def stream():
    def generate():
        for data in crawler.crawl():
            yield f"data: {data}\n\n"

    response = Response(generate(), mimetype="text/event-stream")
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Cache-Control', 'no-cache')
    response.headers.add('Content-Type', 'text/event-stream')
    response.headers.add('Connection', 'keep-alive')
    return response


if __name__ == "__main__":
    app.run(port=5002)