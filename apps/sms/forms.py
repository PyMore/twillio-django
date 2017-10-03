from django import forms
from .models import User


class CreateUserForm(forms.ModelForm):
    """ Create a new user  """
    class Meta:
        model = User
        fields = '__all__'



class SendForm(forms.ModelForm):
    """ Send sms """
    class Meta:
        model = User
        fields = [
            'phone',
        ]