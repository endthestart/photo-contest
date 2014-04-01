from django import forms
from .models import Profile, Event

from multiuploader.forms import MultiuploaderField


class ProfileForm(forms.Form):
    uploadedFiles = MultiuploaderField(required=False)