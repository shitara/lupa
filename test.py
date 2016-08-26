
import lupa

from mongoengine.document import Document
from mongoengine import fields, connect, Q

connect('test', host='192.168.33.2')

class Test(Document):
    name = fields.StringField()
    def __unicode__(self):
        return self.name
class Query(Q):

    def __init__(self, kwargs):
        super().__init__(**kwargs)

    def and_(self, q):
        return self & q

    def or_(self, q):
        return self | q

lua = lupa.LuaRuntime(unpack_returned_tuples=True)

q = Query(dict(
    name = 'kato yamada',
    )).or_(Query(dict(
        name = 'taro yamada',
        )))


lua.globals()['test'] = Test
lua.globals()['Q'] = Query
lua.eval("(function() q = Q({ name = 'kato yamada' }).or_(Q({ name = 'taro yamada' })) end)()")
lua.eval("(function() v,e = test.objects.filter(q) end)()")
lua.eval('print(v)')


