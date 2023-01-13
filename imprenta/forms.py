from django import forms
from django.contrib.auth.forms import UserCreationForm #formulario que viene incluido para crear usuario, con verificacion de contraseña
from django.contrib.auth.admin import User

class UsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=20)

    class Meta: #vinculamos a que modelo hacemos referencia
        model = User #este modelo viene de la migracion de django
        fields = ['username', 'password1', 'password2'] #username es creacion de usuario

