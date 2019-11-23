from django import forms


class TelegramRegistirationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=25)
    password = forms.CharField(label='Passowrd', max_length=25, widget=forms.PasswordInput)
