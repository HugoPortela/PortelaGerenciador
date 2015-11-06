from django import forms
from django.contrib.auth.models import User

from .models import UserProfile,ProdutoProfiles

class UserForm(forms.ModelForm):
    #first_name = forms.CharField(widget=forms.TextInput(attrs={'required': 'required'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'data_cadastro')

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = ProdutoProfiles
        fields = ('nome', 'referencia','quantidade','categoria','preco')
