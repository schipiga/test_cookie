# coding: utf-8

'''
Приложение, чтобы проверить
запрет передачи куки на чужой домен
'''

from features.steps.helpers import urls, ALIEN_HOST, ALIEN_PORT
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route(urls.return_cookies)
def return_cookies():
    return jsonify(request.cookies)


if __name__ == "__main__":
    app.run(host=ALIEN_HOST, port=ALIEN_PORT)
