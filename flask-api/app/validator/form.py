from wtforms import IntegerField,StringField
from app.validator.base import BaseForm as Form
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.libs.enum import ClientTypeEnum
from app.models.user import User


class ClientForm(Form):
    account = StringField(validators=[DataRequired(message='邮箱不能为空'),
                                      Email(message='邮箱格式不正确')])
    password = StringField(validators=[DataRequired()])

    type = IntegerField(validators=[DataRequired()])

    def validate_type(self,value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(Form):


    password = StringField(validators=[DataRequired(message='密码不能为空'),
                                       Regexp(r'^[a-zA-Z0-9_*&$#@]{6,22}$')])

    username = StringField(validators=[DataRequired(message='用户名不能为空'),
                                       length(min=3, max=8, message='字符长度为3-8位')])

    def validate_account(self,value):
        if User.query.filter_by(email=value.data).first:
            raise ValidationError()




