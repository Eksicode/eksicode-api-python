from django.contrib.auth import backends, get_user_model
from django.db.models import Q


class ModelBackend(backends.ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            User().set_password(password)
