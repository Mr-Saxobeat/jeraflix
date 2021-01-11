from django import forms
from django_registration.forms import RegistrationForm
from accounts.models import CustomAccount

class AccountForm(RegistrationForm):
    birthday = forms.DateField(label='Data de nascimento')

    class Meta(RegistrationForm.Meta):
        model = CustomAccount
        fields = ('email', 'password1', 'password2', 'username', 'birthday')

class LoginAccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = CustomAccount
        fields = ('email', 'password')