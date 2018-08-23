from flask import request

from app.libs.enum import ClientTypeEnum
from app.libs.myprint import Myprint
from app.models.user import User
from app.validator.form import ClientForm, UserEmailForm

api = Myprint('register')

@api.route('',methods=['POST'])
def register():

    form = ClientForm().validate_for_api()
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL:__register_user_by_email
        }

        promise[form.type.data]()
    else:
        return str(form.errors)
    return 'sucess'

def __register_user_by_email():

    form = UserEmailForm().validate_for_api()
    User.register_by_email(
        form.username.data,
        form.account.data,
        form.password.data,
    )