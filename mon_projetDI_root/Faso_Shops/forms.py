from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]


        
def validate_name(nom):
    # check if they are numbers in the name
    if (nom.isalpha() == False):
        print("le nom est invalide")  
        raise forms.ValidationError(f'le nom {nom} est invalide')


def validate_prename(prenom):
    # check if they are numbers in the name
    if (prenom.isalpha() == False):
        print("le nom est invalide")  
        raise forms.ValidationError(f'le nom {prenom} est invalide')

class ContactForm(forms.Form):
    #items=forms.CharField.as_hidden()
    nom = forms.CharField(required=False,validators=[validate_name])
    prenom = forms.CharField(required=False,validators=[validate_prename])
    email = forms.EmailField()
    ville = forms.CharField(required=False) 
    pays = forms.CharField(required=False)
    telephone = forms.CharField(required=False)
    