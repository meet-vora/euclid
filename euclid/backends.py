from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileAuthBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username=username)

            if password == user.password:
                userprofile = UserProfile.objects.get(user=user)
                return userprofile
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserProfile.objects.get(pk=user_id)
        except UserProfile.DoesNotExist:
            return None
