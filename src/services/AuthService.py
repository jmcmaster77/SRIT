from .models.User import User


class AuthService():

    @classmethod
    def login_user(cls, user):

        authenticated_user = None

        if user.username == "Ray" and user.password == "ray12345":
            authenticated_user = User(1, "Ray", None, "Ray Perez")
        return authenticated_user
