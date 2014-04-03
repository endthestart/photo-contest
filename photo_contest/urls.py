from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin

from .views import jfu_upload, thumb

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'photo_contest.views.contest_home', name='contest_home'),
    url(r'^wors/$', 'photo_contest.views.wors', name='wors'),
    url(r'^upload/$', jfu_upload, name='jfu_upload'),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
