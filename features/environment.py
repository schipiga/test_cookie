# coding: utf-8

import os
import subprocess

from selenium import webdriver

DRIVER_FILE = 'chromedriver'
DRIVER_PATH = os.path.join(os.curdir, DRIVER_FILE)
PROTOCOL = 'http'
HOST = 'localhost'
PORT = 5000


def before_all(context):
    context.server = subprocess.Popen(('python', 'my_app.py'))
    context.host = '%s://%s:%s' % (PROTOCOL, HOST, PORT)


def before_scenario(context, scenario):
    context.chrome = webdriver.Chrome(DRIVER_PATH)


def after_scenario(context, scenario):
    context.chrome.quit()


def after_all(context):
    context.server.kill()
