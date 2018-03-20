from django import forms

from new_app.models import Obstacle


class LoginForm (forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class NewUserForm(forms.Form):
    login = forms.CharField(label='login')
    password = forms.CharField(label='hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='powtórz hasło', widget=forms.PasswordInput)
    first_name = forms.CharField(label='imie')
    last_name = forms.CharField(label='nazwisko')
    email = forms.EmailField(label='email')


class ObstacleForm(forms.ModelForm):
    class Meta:
        model = Obstacle
        widgets = {'elements': forms.CheckboxSelectMultiple()}
        fields = ('name', 'elements', 'color')
