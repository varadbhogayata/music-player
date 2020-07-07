from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate

class UserLoginForm(forms.Form):
    # username = forms.CharField()
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate','placeholder': 'Enter Username'}))
    # password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist!")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password!")
            if not user.is_active:
                raise forms.ValidationError("This user is not active")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), required=False)
    # password = forms.CharField(
    #     help_text='<ul>Your password can’t be too similar to your other personal information.Your password must contain at least 8 characters.Your password can’t be a commonly used password. Your password can’t be entirely numeric.</ul>',
    #     widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Reenter Password'}))
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
