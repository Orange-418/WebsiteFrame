from django import forms

class RegisterForm(forms.Form):
    # Email field with a class of 'form-control' for styling
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    # Text field for the username with a class of 'form-control' for styling
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    # Password field with a class of 'form-control' for styling
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    # Password field for password confirmation with a class of 'form-control' for styling
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    # Text field for the first name with a class of 'form-control' for styling
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    # Text field for the last name with a class of 'form-control' for styling
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
