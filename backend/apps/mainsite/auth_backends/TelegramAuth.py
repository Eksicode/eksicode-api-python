from ...core.models.user import User
from django.conf import settings


class AuthBackend:

    def authenticate(self, request, username=None):
        try:
            user = User.objects.get(telegram_username=username)
            return user
        except User.DoesNotExist:
            return None

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None