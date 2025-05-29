from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Usuario

class RegistroFormPersonalizado(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Apellidos'})
    )
    fecha_nacimiento = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    telefono = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Número de teléfono'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'})
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'fecha_nacimiento', 'telefono', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''

class LoginFormPersonalizado(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))