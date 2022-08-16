
from django import forms
from .models import profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column


class Profile(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'خانوادگی نام'}))
