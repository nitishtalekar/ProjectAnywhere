from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

class SignupForm(forms.Form):
    email = forms.EmailField()
    user_name = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    reenter_password = forms.CharField(widget = forms.PasswordInput)

class AddProject(forms.Form):
    email = forms.EmailField()
    user_name = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    reenter_password = forms.CharField(widget = forms.PasswordInput)