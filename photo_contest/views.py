import os

from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.http import require_POST

from .forms import EventForm, ProfileForm
from .models import Event, Profile, Photo

from jfu.http import upload_receive, UploadResponse, JFUResponse


def contest_home(request, template_name="contest_home.html"):
    form = ProfileForm()
    context = {
        'form': form,
    }
    return render_to_response(template_name, context, RequestContext(request))


@require_POST
def jfu_upload(request):
    event = get_object_or_404(Event, id=request.session['event_id'])
    profile = get_object_or_404(Profile, id=request.session['profile_id'])

    uploaded_file = upload_receive(request)

    instance = Photo(
        photo=uploaded_file,
        event=event,
        profile=profile,
    )
    instance.save()

    basename = os.path.basename(instance.photo.path)

    file_dict = {
        'name': basename,
        'size': uploaded_file.size,

        'url': instance.photo.url,
        'thumbnailUrl': instance.get_thumbnail().url,

        #'deleteUrl': reverse('jfu_delete', kwargs={'pk': instance.pk}),
        #'deleteType': 'POST',
    }

    return UploadResponse(request, file_dict)


def wors(request, template_name="base.html"):
    if not request.session.get('profile_id', None):
        return HttpResponseRedirect(reverse('profile'))
    event = get_object_or_404(Event, id=request.session['event_id'])
    profile = get_object_or_404(Profile, id=request.session['profile_id'])
    context = {
        'event': event,
        'profile': profile,
    }
    return render_to_response(template_name, context, RequestContext(request))


def event_view(request, template_name="event.html"):
    initial={'event': request.session.get('event', None)}
    form = EventForm(request.POST or None, initial=initial)
    if request.method == 'POST':
        if form.is_valid():
            request.session['event_id'] = form.cleaned_data['event'].id
            return HttpResponseRedirect(reverse('profile'))
    context = {'form': form,}
    return render_to_response(template_name, context, RequestContext(request))


def profile_view(request, template_name="profile.html"):
    if not request.session.get('event_id', None):
        return HttpResponseRedirect(reverse('event'))

    form = ProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save()
            request.session['profile_id'] = profile.id
            return HttpResponseRedirect(reverse('wors'))
    context = {'form': form,}
    return render_to_response(template_name, context, RequestContext(request))
