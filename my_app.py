# coding: utf-8

from copy import deepcopy
from flask import Flask, Response, request, jsonify

from features.steps.helpers import (
    urls,
    responses,
    simple_cookie,
    changed_cookie,
    expired_cookie,
    pathed_cookie,
    domained_cookie,
    unicoded_cookie,
)
from features.environment import HOST, PORT

app = Flask(__name__)


@app.route(urls.set_cookie)
def set_cookie():
    response = Response()
    response.set_data(responses.set_cookie)
    response.set_cookie(*simple_cookie.values())
    return response


@app.route(urls.change_cookie)
def change_cookie():
    response = Response()
    response.set_data(responses.change_cookie)
    response.set_cookie(*changed_cookie.values())
    return response


@app.route(urls.expired_cookie)
def expire_cookie():
    response = Response()
    response.set_data(responses.expired_cookie)
    cookie = deepcopy(expired_cookie)
    name = cookie.pop('name')
    response.set_cookie(name, **cookie)
    return response


@app.route(urls.pathed_cookie)
def path_cookie():
    response = Response()
    response.set_data(responses.pathed_cookie)
    cookie = deepcopy(pathed_cookie)
    name = cookie.pop('name')
    response.set_cookie(name, **cookie)
    return response


@app.route(urls.return_cookies)
def return_cookies():
    return jsonify(request.cookies)


@app.route(urls.path_to_cookie)
def path_to_cookie():
    return jsonify(request.cookies)


@app.route(urls.foreign_cookie)
def foreign_cookie():
    response = Response()
    response.set_data(responses.domained_cookie)
    cookie = deepcopy(domained_cookie)
    name = cookie.pop('name')
    response.set_cookie(name, **cookie)
    return response


@app.route(urls.unicode_cookie)
def unicode_cookie():
    response = Response()
    response.set_cookie(*unicoded_cookie.values())
    return response


@app.route(urls.null_cookie)
def null_cookie():
    response = Response()
    response.set_cookie('', '')
    return response


@app.route(urls.long_cookie)
def long_cookie():
    response = Response()
    response.set_cookie('long cookie', 1000000 * 'a')
    return response


@app.route(urls.many_cookies)
def many_cookies():
    response = Response()
    for i in xrange(10000):
        response.set_cookie('cookie_%i' % i, 'value_%i' % i)
    return response


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
