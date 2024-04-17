import datetime
import pytz
import jwt

jwt_key = "JWTKEY15332"


class Security():
    jwt_key = "JWTKEY15332"
    tz = pytz.timezone("America/Caracas")

    @classmethod
    def generate_token(cls, authenticated_user):
        payload = {
            'iat': datetime.datetime.now(tz=cls.tz),
            'exp': datetime.datetime.now(tz=cls.tz)+datetime.timedelta(days=180),
            'usernamer': authenticated_user.username,
            'fullname': authenticated_user.fullname
        }
        return jwt.encode(payload, cls.jwt_key, algorithm="HS256")

    @classmethod
    def verivy_token(cls, headers):
        if "Authorization" in headers.keys():
            autorization = headers["Authorization"]
            encoded_token = autorization.split(" ")[1]
            if (len(encoded_token) > 0):

                try:
                    payload = jwt.decode(
                        encoded_token, cls.jwt_key, algorithms=["HS256"])
                    return True
                except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError, jwt.InvalidTokenError):
                    return False
        return False
