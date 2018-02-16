from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


# A quick note to watch out for in the next lecture.
# I accidentally named a form the same name as the model.
#  Specifically the UserProfileInfo model. The ModelForm
#  that relates to it should have a different name, like:
#  UserProfileInfoForm. This is fixed in the Registration
#  lecture (I talk about it and point it out) and it is
#  also correct in the downloaded note files. So keep this
#  in mind when you see me create that second form!
