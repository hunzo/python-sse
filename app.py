from datetime import datetime
from flask import Flask, render_template, jsonify
from flask.wrappers import Response
import time


app = Flask(__name__)

COUNTER = 0


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/stream")
def stream():
    def get_data():
        while True:
            time.sleep(0.5)
            yield f'data: {datetime.now()} \n\n'

    return Response(get_data(), mimetype='text/event-stream')


@app.post("/increase")
def increase():
    global COUNTER
    COUNTER = COUNTER + 1
    print(COUNTER)
    ret = {
        "status": "increase",
        "counter": COUNTER
    }
    return jsonify(ret)


@app.post("/decrease")
def decrease():
    global COUNTER
    COUNTER = COUNTER - 1
    print(COUNTER)
    ret = {
        "status": "decrease",
        "counter": COUNTER
    }
    return jsonify(ret)


if __name__ == "__main__":
    app.run(debug=True)
