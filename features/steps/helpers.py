# coding: utf-8


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


urls = AttrDict({
    'set_cookie': '/set_cookie',
    'change_cookie': '/change_cookie',
    'expired_cookie': '/expired_cookie',
    'return_cookies': '/return_cookies',
    'pathed_cookie': '/pathed_cookie',
    'path_to_cookie': '/path_to_cookie',
    'foreign_cookie': '/foreign_cookie',
    'unicode_cookie': '/unicode_cookie',
    'long_cookie': '/long_cookie',
    'many_cookies': '/many_cookies',
    'null_cookie': '/null_cookies',
})

asserts = AttrDict({
    'cookie_not_found': u'Cookie не найдено',
    'name_not_found': u'Имя cookie не найдено',
    'value_not_found': u'Значение cookie не найдено',
    'cookie_still_present': u'Cookie не удалена',
    'cookies_still_present': u'Cookies не удалились',
    'cookie_not_expired': u'Истекшая cookie не исчезла',
    'server_still_alive': u'Сервер до сих пор еще жив?!',
})

me = u'<span style="color: red"><b>Я</b></span> - страничка'

responses = AttrDict({
    'set_cookie': u'%s, устанавливающая cookie' % me,
    'change_cookie': u'%s, изменяющая cookie' % me,
    'expired_cookie': u'%s, устанавливающая cookie c лимитом жизни' % me,
    'pathed_cookie': u'%s, устанавливающая cookie для определенного адреса хоста' % me,
    'domained_cookie': u'%s, устанавливающая cookie для определенного домена' % me,
})

simple_cookie = {
    'name': 'Cookie_name',
    'value': 'Cookie_value',
}
changed_cookie = {
    'name': 'Cookie_name',
    'value': 'Changed_cookie_value',
}
expired_cookie = {
    'name': 'Expired_cookie',
    'value': 'expired cookie value',
    'max_age': 2,
}
pathed_cookie = {
    'name': 'Cookie_name',
    'value': 'Cookie_value',
    'path': '/path_to_cookie',
}

domained_cookie = {
    'name': 'Cookie_name',
    'value': 'Cookie_value',
    'domain': '127.0.0.1:9999',
}

unicoded_cookie = {
    'name': 'Cookie_name',
    'value': u'Я - юникодная кука',
}
