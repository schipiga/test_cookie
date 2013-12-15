# coding: utf-8

'''
version: 0.1
date: 14.12.2013
author: Sergey Chipiga <chipiga86@mail.ru>
'''

import time
import json
import subprocess

from behave import when, then
from helpers import (
    urls,
    asserts,
    simple_cookie,
    changed_cookie,
    expired_cookie,
    unicoded_cookie,
    ALIEN_HOST,
    ALIEN_PORT,
)

COOKIES_LIMIT = 500  # для проверки максимального количества принимаемых кук


@when(u'я открываю страницу, отдающую куку')
def step(context):
    context.chrome.get(context.host + urls.set_cookie)


@when(u'я открываю страницу, изменяющую куку')
def step(context):
    context.chrome.get(context.host + urls.change_cookie)


@when(u'я удаляю куку по имени')
def step(context):
    context.chrome.delete_cookie(simple_cookie['name'])


@when(u'я удаляю все куки браузера')
def step(context):
    context.chrome.delete_all_cookies()


@when(u'я открываю страницу, отдающую истекающую куку')
def step(context):
    context.chrome.delete_all_cookies()
    context.chrome.get(context.host + urls.expired_cookie)


@when(u'я жду, пока кука истечет')
def step(context):
    time.sleep(expired_cookie['max_age'] + 1)


@when(u'я отправляю запрос на страницу, отдающую список полученных кук')
def step(context):
    context.chrome.get(context.host + urls.return_cookies)


@when(u'я закрываю браузер')
def step(context):
    context.chrome.close()


@when(u'я открываю браузер заново')
def step(context):
    context.chrome = context.web_driver.Chrome(context.driver_path)


@when(u'я открываю страницу, отдающую куку с определенным адресом')
def step(context):
    context.chrome.delete_all_cookies()
    context.chrome.get(context.host + urls.pathed_cookie)


@when(u'я открываю страницу, отдающую куку для чужого домена')
def step(context):
    context.chrome.delete_all_cookies()
    context.chrome.get(context.host + urls.foreign_cookie)


@when(u'я открываю страницу, отдающую куку в виде utf-8 символов')
def step(context):
    context.chrome.get(context.host + urls.unicode_cookie)


@when(u'я открываю страницу, передающую в куке пустые строки')
def step(context):
    context.chrome.get(context.host + urls.empty_cookie)


@when(u'я устанавливаю МНОГО кук')
def step(context):
    # просто посетим любую страничку и затем удалим куки
    # т.к. chromedriver не позволяет открыть браузер и
    # сразу устанавливать куки
    context.chrome.get(context.host + urls.set_cookie)
    context.chrome.delete_all_cookies()
    [context.chrome.add_cookie(
        {'name': 'cookie_%i' % i, 'value': 'cookie_%i' % i}
    ) for i in xrange(COOKIES_LIMIT)]


@when(u'я открываю страницу, отдающую другую куку')
def step(context):
    context.chrome.get(context.host + urls.expired_cookie)


@when(u'я открываю страницу, отдающую куку ОГРОМНОЙ длины')
def step(context):
    context.chrome.get(context.host + urls.long_cookie)


@then(u'в браузере устанавливается кука')
def step(context):
    cookies = context.chrome.get_cookies()
    assert len(cookies) == 1, asserts.expected_one_cookie
    assert cookies[0]['name'] == simple_cookie['name'], \
        asserts.name_not_found
    assert cookies[0]['value'] == simple_cookie['value'], \
        asserts.value_not_found


@then(u'в браузере будет измененная кука')
def step(context):
    cookies = context.chrome.get_cookies()
    assert len(cookies) == 1, asserts.expected_one_cookie
    assert cookies[0]['name'] == changed_cookie['name'], \
        asserts.name_not_found
    assert cookies[0]['value'] == changed_cookie['value'], \
        asserts.value_not_found


@then(u'в браузере будет кука содержащая utf-8 символы')
def step(context):
    cookies = context.chrome.get_cookies()
    assert cookies[0]['value'] == unicoded_cookie['value'], \
        asserts.value_not_found


@then(u'в браузере будет пустая кука')
def step(context):
    cookie = context.chrome.get_cookies()[1]
    assert cookie.get('value', None) == '', asserts.value_not_found


@then(u'у меня отваливается сервер :)')
def step(context):
    assert 'IDR_ERROR_NETWORK_GENERIC' in context.chrome.page_source, \
        asserts.server_still_alive


@then(u'у меня количество кук ограничено')
def step(context):
    assert len(context.chrome.get_cookies()) < COOKIES_LIMIT, asserts.many_cookies


@then(u'в браузере будет "{count}" куки')
def step(context, count):
    cookies = context.chrome.get_cookies()
    assert len(cookies) == int(count), asserts.cookie_not_found


@then(u'эта кука не будет передаваться другим страницам')
def step(context):
    context.chrome.get(context.host + urls.return_cookies)
    assert not json.loads(context.json_page()), asserts.cookie_still_present


@then(u'эта кука не будет передаваться своему домену')
def step(context):
    context.chrome.get(context.host + urls.return_cookies)
    assert not json.loads(context.json_page()), asserts.cookie_still_present


@then(u'эта кука не будет передаваться чужому домену')
def step(context):
    # запустим другое приложение на другом порту
    server = subprocess.Popen(('python', 'alien_app.py'))
    # подождем пока оно стартанет
    time.sleep(2)
    # попробуем передать куку на внешний домен
    context.chrome.get(
        'http://%s:%s' % (ALIEN_HOST, ALIEN_PORT) + urls.return_cookies)
    server.kill()
    assert not json.loads(context.json_page()), asserts.cookie_still_present


@then(u'в браузере не остается этой куки')
def step(context):
    assert not context.chrome.get_cookie(simple_cookie['name']), \
        asserts.cookie_still_present


@then(u'я не получу ни одной куки в ответ')
def step(context):
    assert not json.loads(context.json_page()), asserts.cookie_not_expired


@then(u'у меня не остается кук')
def step(context):
    assert not context.chrome.get_cookies(), asserts.cookies_still_present


@then(u'эта кука будет передаваться другим страницам хоста')
def step(context):
    context.chrome.get(context.host + urls.return_cookies)
    assert json.loads(context.json_page()), asserts.cookie_not_found


@then(u'эта кука будет передаваться по этому адресу')
def step(context):
    context.chrome.get(context.host + urls.path_to_cookie)
    assert json.loads(context.json_page()), asserts.cookie_not_found
