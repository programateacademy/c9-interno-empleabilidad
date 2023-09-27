
from django import forms
from django.contrib.auth import authenticate
from Dashboard.models.student import Estudiante

class EstudianteLoginForm(forms.Form):
    username_or_dni = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username_or_dni = cleaned_data.get('username_or_dni')
        password = cleaned_data.get('password')

        if username_or_dni and password:
            # Intenta autenticar por username
            user = authenticate(username=username_or_dni, password=password)
            if user is None:
                # Si la autenticación por username falla, intenta por dni
                try:
                    estudiante = Estudiante.objects.get(dni=username_or_dni)
                    user = authenticate(username=estudiante.user.username, password=password)
                except Estudiante.DoesNotExist:
                    pass

            if user is None:
                raise forms.ValidationError("Los detalles de inicio de sesión no son válidos")

        return cleaned_data
