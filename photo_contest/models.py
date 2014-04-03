from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer


class Profile(models.Model):
    """
    Profile information for uploaded content
    """
    full_name = models.CharField(
        _("full name"),
        max_length=255,
        blank=False,
        null=False,
        help_text=("The full name."),
    )
    email = models.EmailField(
        _("email"),
        max_length=255,
        blank=False,
        null=False,
        help_text=_("The email."),
    )
    phone = models.CharField(
        _("phone number"),
        blank=True,
        max_length=30,
        help_text=_("The phone number."),
    )

    copyright = models.TextField(
        _("copyright"),
        max_length=1000,
        help_text=_("The copyright information."),
    )

    def __unicode__(self):
        return u"{}".format(self.full_name)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")


class Event(models.Model):
    """
    Event information for uploading photos.
    """
    title = models.CharField(
        _("title"),
        max_length=255,
        blank=False,
        null=False,
        help_text=_("The name of the event."),
    )
    slug = models.SlugField(
        _("slug"),
        help_text=_("Used for URLs, auto-generated from title if blank"),
        blank=True,
        null=True,
    )
    date = models.DateField(
        _("date"),
    )

    def save(self, **kwargs):
        if self.title and not self.slug:
            self.slug = slugify(self.name)

    @models.permalink
    def get_absolute_url(self):
        return False

    def __unicode__(self):
        return u"{}".format(self.title)

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")


def photo_upload_to(instance, filename):
    return '{}/{}/{}'.format(settings.PHOTO_UPLOAD_TO, 'none', filename)

def thumbnail_upload_to(instance, filename):
    return '{}/{}/{}'.format(settings.PHOTO_UPLOAD_TO, 'none/thumbnails', filename)


class Photo(models.Model):
    photo = models.ImageField(
        _("photo"),
        upload_to=photo_upload_to,
    )
    thumbnail = ThumbnailerImageField(
        upload_to=thumbnail_upload_to,
        resize_source=dict(size=(100, 100)),
        blank=True,
        null=True,
    )
    event = models.ForeignKey(
        Event,
        blank=True,
        null=True,
    )
    profile = models.ForeignKey(
        Profile,
        blank=True,
        null=True,
    )

    @models.permalink
    def get_absolute_url(self):
        return reverse('photo_thumb', (), {
            'photo_id': self.id,
        })
