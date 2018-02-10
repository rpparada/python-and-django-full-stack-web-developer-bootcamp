from django import forms
from nivel3_app.models import Usuarios

class UsusarioFormulario(forms.ModelForm):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    nombreCarrera = forms.CharField()

    class Meta:
        model = Usuarios
        fields = '__all__'

class TituloFormulario(forms.Form):
    nombreCarrera = forms.CharField()
    duracion = forms.IntegerField()
