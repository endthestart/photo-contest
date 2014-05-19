from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
from .forms import EventForm, ProfileForm


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'photo_contest.views.contest_home', name='contest_home'),
    url(r'^submit/$', 'photo_contest.views.submit', name='submit'),
    url(r'^event/$', 'photo_contest.views.event_view', name='event'),
    url(r'^profile/$', 'photo_contest.views.profile_view', name='profile'),
    url(r'^upload/$', 'photo_contest.views.jfu_upload', name='jfu_upload'),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
