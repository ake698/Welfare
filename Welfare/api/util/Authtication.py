from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed,APIException
from rest_framework.permissions import BasePermission

from api.models import UserToken


def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()




class Authtication(BaseAuthentication):
    def authenticate(self, request):
        token = request._request.headers.get('Authorization')
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise AuthenticationFailed("用户认证失败！")
        return token_obj.user, token_obj

    def authenticate_header(self, request):
        # BaseAuthentication
        return "Basic relm-'api'"


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == 3:
            return True
        return False