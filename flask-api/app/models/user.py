from sqlalchemy import Column, Integer,String,SmallInteger

from app.libs.error_code import NotFound
from app.models.base import Base,db

from werkzeug.security import generate_password_hash,check_password_hash

class User(Base):
    id = Column(Integer,primary_key=True)
    username = Column(String(24),unique=True)
    mobile = Column(Integer,unique=True)
    email = Column(String(50),unique=True)
    auth = Column(SmallInteger,default=1)
    _password = Column('password',String(100))

    def keys(self):
        return ['id','email','mobile','username','auth']


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(username,email,password):
        with db.auto_commit():
            user = User()
            user.username = username
            user.email = email
            user.password = password
            db.session.add(user)

    @staticmethod
    def verify(email,password):
        user = User.query.filter_by(email=email).first()
        if not user:
            raise NotFound(msg='用户不存在')
        if not user.check_password(password):
            raise NotFound(msg='密码错误')
        scope= 'AdminScope' if user.auth==2 else 'UserScope'
        return {'uid':user.id,'scope':scope}



    def check_password(self,raw):
        if not self._password:
            return False
        return check_password_hash(self._password,raw)








