from app.libs.error import APIException

class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 10086

class ParameterException(APIException):
    code = 400
    msg = 'invalid'
    error_code = 1000

class NotFound(APIException):
    code = 404
    msg = 'user is not found'
    error_code = 4040

class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1002

class JSONFailed(APIException):
    code = 450
    msg = 'JSONEncode is not have keys and getitem'
    error_code = 1111

class DeleteSucess(APIException):
    code = 402
    msg = 'account is delete'
    error_code = 4444

class Forbidden(APIException):
    code =403
    error_code = 1004
    msg = 'forbidden, not in scope'
