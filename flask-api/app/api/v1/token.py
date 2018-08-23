from flask import current_app, jsonify

from app.libs.enum import ClientTypeEnum
from app.libs.myprint import Myprint
from app.models.user import User

from app.validator.form import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

api = Myprint('login')

@api.route('',methods=['POST'])
def login():
    form = ClientForm().validate_for_api()

    promise={
        ClientTypeEnum.USER_EMAIL:User.verify
    }
    identify = promise[(ClientTypeEnum(form.type.data))](
        form.account.data,
        form.password.data,
    )



    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identify['uid'],
                                form.type.data,
                                identify['scope'],
                                expiration)
    t = {
        'token':token.decode('ascii')
    }
    return jsonify(t)


def generate_auth_token(uid,ac_type,scope=None,
                        expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps({
        'uid':uid,
        'type':ac_type.value,
        'scope':scope
    })
