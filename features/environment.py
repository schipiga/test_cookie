# coding: utf-8

import os
import re
import time
import subprocess

from selenium import webdriver

# FIXME: не использовать относительные пути
DRIVER_FILE = 'chromedriver'
DRIVER_PATH = os.path.join(os.curdir, DRIVER_FILE)
PROTOCOL = 'http'
HOST = 'localhost'
PORT = 5000


def before_all(context):
    context.server = subprocess.Popen(('python', 'my_app.py'))
    # подождем пока сервер стартует
    time.sleep(2)
    context.host = '%s://%s:%s' % (PROTOCOL, HOST, PORT)
    # сохраним в контекте, т.к. нужно будет открыть один экземпляр в тесте
    context.driver_path = DRIVER_PATH
    context.web_driver = webdriver
    #FIXME: flask doesn't return json without html tags :(
    context.json_page = lambda: re.sub(
        '<[^<]+?>', '', context.chrome.page_source)


# TODO: подумать над тем правильно ли в каждом сценарии запускать браузер
def before_scenario(context, scenario):
    context.chrome = webdriver.Chrome(DRIVER_PATH)


def after_scenario(context, scenario):
    context.chrome.quit()


def after_all(context):
    context.server.kill()
