from django import forms
from .models import Profile, Event


class ProfileForm(forms.Form):
    class Meta:
        model = Profile