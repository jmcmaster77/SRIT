import datetime
import pytz
import jwt

from config.config import ks


class Security():
    jwt_key = ks
    tz = pytz.timezone("America/Caracas")

    @classmethod
    def generate_token(cls, authenticated_user):
        payload = {
            'iat': datetime.datetime.now(tz=cls.tz),
            'exp': datetime.datetime.now(tz=cls.tz)+datetime.timedelta(days=180),
            'id': authenticated_user.id,
            'usernamer': authenticated_user.username,
            'fullname': authenticated_user.fullname,
            'roles': ['admin', 'edit']
        }
        return jwt.encode(payload, cls.jwt_key, algorithm="HS256")

    @classmethod
    def verify_token(cls, headers):
        if "authorization" in headers.keys():
            autorization = headers["authorization"]
            encoded_token = autorization.split(" ")[1]
            if (len(encoded_token) > 0):

                try:
                    payload = jwt.decode(
                        encoded_token, cls.jwt_key, algorithms=["HS256"])
                    roles = list(payload['roles'])
                    if "admin" in roles:
                        return True
                    return False
                except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError, jwt.InvalidTokenError):
                    return False
        return False

    @classmethod
    def virify_token_r(cls, token):
        
        if (len(token) > 0):

            try:
                payload = jwt.decode(
                    token, cls.jwt_key, algorithms=["HS256"])
                roles = list(payload['roles'])
                if "admin" in roles:
                    return True
                return False
            except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError, jwt.InvalidTokenError):
                return False
        
