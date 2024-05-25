from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.core import validators
from Menu.models import Menu, Perfil, Mesa

class FormUser(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(5)])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput)
    
    #Función para verificar que los datos en atrapabots están bien
    def clean_botcatcher(self):
        atrapador = self.cleaned_data['botcatcher']
        if (len(atrapador) > 0):
            raise forms.ValidationError("Ese mi EL BOT!")
        return atrapador


class Form_Comments(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['Nombre', 'Descripcion', 'imagen']

class RegistroForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=150, help_text='')
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))
    num_mesa = forms.IntegerField(label='Número de mesa', required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            if self.cleaned_data.get('num_mesa'):
                mesa = Mesa.objects.create(numero_mesa=self.cleaned_data['num_mesa'])
                mesa.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label='Contraseña',
        strip=False,
        widget=forms.PasswordInput
    )