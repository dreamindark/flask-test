from flask import jsonify, g

from app.libs.error_code import DeleteSucess
from app.libs.myprint import Myprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Myprint('user')

@api.route('/<int:uid>',methods=['GET'])
@auth.login_required
def super_get_user(uid):

    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)

@api.route('/<int:uid>',methods=['DELETE'])
@auth.login_required
def super_delete_user(uid):
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSucess()

@api.route('',methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)

@api.route('',methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSucess()