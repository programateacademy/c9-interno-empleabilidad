from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from Dashboard.models.student import Estudiante

class EstudianteAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Intenta autenticar primero usando el campo "username"
            user = UserModel.objects.get(username=username)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            # Si no se encontró un usuario por "username", intenta con "DNI"
            try:
                estudiante = Estudiante.objects.get(dni=username)
                user = estudiante.user
                if user.check_password(password):
                    return user
            except Estudiante.DoesNotExist:
                # No se encontró un estudiante con este DNI o username
                pass

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
