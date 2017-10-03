from django import forms
from .models import User, Sendedsms


class CreateUserForm(forms.ModelForm):
    """ Create a new user  """
    class Meta:
        model = User
        fields = '__all__'

        widgets={
            'phone': forms.TextInput(attrs={
                'type': 'text',
                'required':'true',
                'class':'form-control'
            }),
            'username': forms.TextInput(attrs={
                'type': 'text',
                'required':'true',
                'class':'form-control'
            }),
            'email': forms.TextInput(attrs={
                'type': 'text',
                'required':'true',
                'class':'form-control'
            }),
            'password': forms.TextInput(attrs={
                'type': 'text',
                'required':'true',
                'class':'form-control'
            }),            
            'first_name': forms.TextInput(attrs={
                'type': 'text',
                'required':'true',
                'class':'form-control'
            }),            

            'last_name': forms.TextInput(attrs={
                'type': 'text',
                'required':'true',
                'class':'form-control'
            }),            

            'last_login': forms.TextInput(attrs={
                'type': 'text',
                'required':'true',
                'class':'form-control'
            }),            


            'is_active': forms.TextInput(attrs={
                'type': 'checkbox',
                'required':'true',
                'class':'form-control'
            }),    

        }


class SendFormForm(forms.ModelForm):
    """ Send sms """
    class Meta:
        model = Sendedsms
        fields = '__all__'


