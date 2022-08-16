
#from django import forms
# Import our django mddouls we have to use
from django import forms
from django.contrib.auth.models import User
from registration.models import UserProfileInfo
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'خانوادگی نام'}))

    class Meta():
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('id_nummber', 'phone_nummber')

    def clean(self):
        clened_data = super().clean()
        user_name = clened_data.get("username", None)
        id_nummber = clened_data.get("id_nummber", None)

        try:
            user_name != id_nummber
        except:
            raise ValidationError(
                'فیلد username باید با شماره دانشجویی برابر نیست.', code='username and id_nummber')

    def save(self, clean, commit: True):
        self.clean()
        return super().save(commit=commit)
