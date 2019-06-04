from rest_framework.authtoken.models import Token
from django.contrib.auth import login, get_user_model

User = get_user_model()

def login_user(request, token):
    """
    Make sure that the token is associated with a user
    """
    if token is None:
        return None
    user_token = Token.objects.get(key=token)
    user = User.objects.get(id=user_token.user_id)
    if user is None:
        return None
    login(request, user)
