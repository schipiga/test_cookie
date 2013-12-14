# coding: utf-8

import os

from selenium import webdriver

DRIVER_FILE = 'chromedriver'
DRIVER_PATH = os.path.join(os.curdir, DRIVER_FILE)
HOST = 'http://localhost'
PORT = 5000


def before_all(context):
    context.host = '%s:%s' % (HOST, PORT)


def before_scenario(context, scenario):
    context.chrome = webdriver.Chrome(DRIVER_PATH)


def after_scenario(context, scenario):
    context.chrome.quit()
