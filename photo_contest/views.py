from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from multiuploader.forms import MultiUploadForm
from .forms import ProfileForm


def contest_home(request, template_name="contest_home.html"):
    form = ProfileForm()
    context = {
        'uploadForm': MultiUploadForm(),
        'form': form,
    }
    return render_to_response(template_name, context, RequestContext(request))