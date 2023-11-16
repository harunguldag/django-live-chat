from django import forms
# from django.contrib.auth.forms import AuthenticationForm

class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()




class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()


class post_comment(forms.Form):
    
    text = forms.CharField()
