from django import forms
from .models import Secret

class SecretForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Secret
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }