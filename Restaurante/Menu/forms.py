from django import forms
from django.core import validators
from Menu.models import Menu

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
