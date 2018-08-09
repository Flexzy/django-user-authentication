from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Email'
    }))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'First Name'
    }))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Last Name'
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = "<span class='help-text small'>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>"

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = "<ul class='help-text small'><li>Your password can't be too similar to your other personal information.</li> <li>Your password must contain at least 8 characters.</li> <li>Your password can't be a commonly used password.</li> <li>Your password can't be entirely numeric.</li></ul>"

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = "<span class='help-text small'>Enter the same password as before, for verification.</small>"



class EditForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = "<span class='small'>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>"

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['email'].label = ''

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['first_name'].label = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['last_name'].label = ''

        self.fields['password'].label = ''
        self.fields['password'].help_text = "<span class='small'>Raw passwords are not stored, so there is no way to see this user's password, but you can change the password using <a href='/change_password'>this form</a>.</small>"

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Old password',
        'type': 'password'
    }))
    new_password1 = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'New password',
        'type': 'password'
    }), help_text = "<ul class='small'><li>Your password can't be too similar to your other personal information.</li> <li>Your password must contain at least 8 characters.</li> <li>Your password can't be a commonly used password.</li> <li>Your password can't be entirely numeric.</li></ul>")
    new_password2 = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'New password confirmation',
        'type': 'password'
    }))
    