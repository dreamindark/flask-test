from flask import Blueprint
from app.api.v1 import user,register,token,book



def create_api_v1():
    bp_v1 = Blueprint('v1',__name__)
    user.api.register(bp_v1)
    register.api.register(bp_v1)
    token.api.register(bp_v1)
    book.api.register(bp_v1)
    return bp_v1