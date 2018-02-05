from django import forms
from django.core import validators

# def verifica_primera_letra_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('Nombre tiene que comenzar con z')

class FormName(forms.Form):
    name = forms.CharField()
    # name = forms.CharField(validators=[verifica_primera_letra_z])
    email = forms.EmailField()
    verifica_email = forms.EmailField(label='Ingresa tu email nuevamente:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super(forms.Form,self).clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verifica_email']

        if email != vemail:
            raise forms.ValidationError("Ambos correos deben ser iguales")
    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)] )

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("BOT FOUND!!")
    #     return botcatcher
