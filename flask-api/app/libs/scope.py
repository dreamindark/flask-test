
class Scope():
    allow_module=[]
    allow_api=[]

class AdminScope(Scope):
    allow_module = ['v1.user']

class UserScope(Scope):
    allow_api = ['v1.user+get_user',
                 'v1.user+delete_user']

def is_in_scope(scope,endpoint):
    scope = globals()[scope]()
    splits = endpoint.split('+')
    my_name = splits[0]
    if endpoint in scope.allow_api:
        return True
    if my_name in scope.allow_module:
        return True
    return False
