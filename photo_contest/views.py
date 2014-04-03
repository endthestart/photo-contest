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


def thumb(request, photo_id=None, template_name="thumb.html"):
    photo = get_object_or_404(Photo, id=photo_id)
    context = {
        'photo': photo,
    }
    return render_to_response(template_name, context, RequestContext(request))


@require_POST
def jfu_upload(request):
    #import pdb; pdb.set_trace()
    uploaded_file = upload_receive(request)

    instance = Photo(photo=uploaded_file)
    instance.save()

    basename = os.path.basename(instance.photo.path)

    file_dict = {
        'name': basename,
        'size': uploaded_file.size,

        'url': settings.MEDIA_URL + 'photo_upload/none/' + basename,
        'thumbnailUrl': instance.get_absolute_url()

        #'deleteUrl': reverse('jfu_delete', kwargs={'pk': instance.pk}),
        #'deleteType': 'POST',
    }

    return UploadResponse(request, file_dict)
