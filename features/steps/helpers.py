# coding: utf-8


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


urls = AttrDict({
    'set_cookie': '/set_cookie',
    'change_cookie': '/change_cookie',
})


asserts = AttrDict({
    'cookie_not_found': u'Cookie не найдено',
    'name_not_found': u'Имя cookie не найдено',
    'value_not_found': u'Значение cookie не найдено',
})


me = u'<span style="color: red"><b>Я</b></span> - страничка'


responses = AttrDict({
    'set_cookie': u'%s, устанавливающая cookie' % me,
    'change_cookie': u'%s, изменяющая cookie' % me,
})


simple_cookie = {'name': 'Cookie_name', 'value': 'Cookie_value'}
changed_cookie = {'name': 'Cookie_name', 'value': 'Changed_cookie_value'}
