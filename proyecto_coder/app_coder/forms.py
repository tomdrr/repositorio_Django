from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User



class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()


class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput )
    password2 = forms.CharField(label="Repetir Contraseña" , widget=forms.PasswordInput )

    
    class Meta:
        model = User
        fields = ['email' , 'password1' , 'password2']
        help_text = {k:"" for k in fields} 