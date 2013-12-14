# coding: utf-8

'''
version: 0.1
date: 14.12.2013
author: Sergey Chipiga <chipiga86@mail.ru>
'''

from behave import given, when, then
from helpers import urls, asserts, simple_cookie


@when(u'я открываю страницу, отдающую cookies')
def step(context):
    context.chrome.get(context.host + urls.set_cookie)


@then(u'в браузере устанавливается cookies')
def step(context):
    cookies = context.chrome.get_cookies()
    assert len(cookies) == 1, asserts.cookie_not_found
    assert cookies[0].get('name', None) == simple_cookie['name'], asserts.name_not_found
    assert cookies[0].get('value', None) == simple_cookie['value'], asserts.value_not_found
