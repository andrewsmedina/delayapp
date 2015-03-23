from flask import Flask, request

import os
import time


app = Flask(__name__)
app.debug = True


@app.route("/")
def delay():
    delay = request.args.get("delay")
    if delay:
        time.sleep(float(delay))
    return "delay app"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
