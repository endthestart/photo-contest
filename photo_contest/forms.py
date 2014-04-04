from django import forms
from .models import Profile, Event


class EventForm(forms.Form):
    event = forms.ModelChoiceField(queryset=Event.objects.all())


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile