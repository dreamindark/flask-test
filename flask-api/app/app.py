from flask import Flask as _Flask

from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import JSONFailed

class JSONEncoder(_JSONEncoder):
    def default(self,o):
        if hasattr(o,'keys') and hasattr(o,'__getitem__'):
            return dict(o)
        return JSONFailed()


class Flask(_Flask):
    json_encoder = JSONEncoder