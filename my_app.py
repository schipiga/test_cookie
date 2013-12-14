# coding: utf-8

from flask import Flask, Response

from features.steps.helpers import urls, responses, simple_cookie

app = Flask(__name__)


@app.route(urls.set_cookie)
def set_cookie():
    response = Response()
    response.set_data(responses.set_cookie)
    response.set_cookie(*simple_cookie.values())
    return response


if __name__ == "__main__":
    app.run()
