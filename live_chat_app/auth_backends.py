from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

User = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Kullanıcı adı ile veya e-posta ile kimlik doğrulama yapma
            user = User.objects.get(Q(username=username) | Q(email=username))

            # Kullanıcının şifresi doğru ise kullanıcıyı döndür
            if user.check_password(password):
                return user

        except User.DoesNotExist:
            # Kullanıcı bulunamazsa None döndür
            return None

    def get_user(self, user_id):
        try:
            # Kullanıcı kimlik doğrulama işlemi için kullanılır
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
