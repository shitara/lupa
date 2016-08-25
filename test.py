
import lupa

def error():
    raise Exception('er')

class Test:

    def __get_item__(self, a):
        return None

    @classmethod
    def t(cls, msg):
        raise Exception('aa')


lua = lupa.LuaRuntime(unpack_returned_tuples=True)


lua.globals()['test'] = Test
lua.eval("(function() print(('%s'):format('aaa')) end)()")



