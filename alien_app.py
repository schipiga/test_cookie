# coding: utf-8

from features.steps.helpers import urls
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route(urls.return_cookies)
def return_cookies():
    return jsonify(request.cookies)


if __name__ == "__main__":
    app.run(port=9999)
