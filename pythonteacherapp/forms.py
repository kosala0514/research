from django.contrib.auth.hashers import make_password
from django import forms
from pythonteacherapp.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'contact', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Encrypt the password
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
