import os

from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.http import require_POST

from .forms import ProfileForm
from .models import Photo, photo_upload_to

from jfu.http import upload_receive, UploadResponse, JFUResponse


def contest_home(request, template_name="contest_home.html"):
    form = ProfileForm()
    context = {
        'form': form,
    }
    return render_to_response(template_name, context, RequestContext(request))


@require_POST
def jfu_upload(request):
    uploaded_file = upload_receive(request)

    instance = Photo(photo=uploaded_file)
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
    context = {}
    return render_to_response(template_name, context, RequestContext(request))
