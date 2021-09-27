import logging

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from mayan.apps.documents.models import Document
from mayan.apps.events.classes import EventManagerMethodAfter, EventManagerSave
from mayan.apps.events.decorators import method_event

from .events import (
    event_document_review_created, event_document_review_deleted,
    event_document_review_edited
)

logger = logging.getLogger(name=__name__)


class Review(models.Model):
    """
    Model to store one review per document per user per date & time.
    """
    _event_created_event = event_document_review_created
    _event_edited_event = event_document_review_created

    document = models.ForeignKey(
        db_index=True, on_delete=models.CASCADE, related_name='reviews',
        to=Document, verbose_name=_('Document')
    )
    user = models.ForeignKey(
        editable=False, on_delete=models.CASCADE, related_name='reviews',
        to=settings.AUTH_USER_MODEL, verbose_name=_('User'),
    )

    firstName = models.CharField(verbose_name=_('First Name'), max_length=48)
    lastName = models.CharField(verbose_name=_('Last Name'), max_length=48)
    gradYear = models.CharField(verbose_name=_('Graduation Year'), max_length=48)
    fieldOfStudy = models.CharField(verbose_name=_('Field of Study'), max_length=48)

    gpaScale = models.IntegerField(verbose_name=_('GPA: Rate 1-10'))
    technicalScale = models.IntegerField(verbose_name=_('Technical Skills: Rate 1-10'))
    communicationScale = models.IntegerField(verbose_name=_('Communication Skills: Rate 1-10'))
    experienceScale = models.IntegerField(verbose_name=_('Experience: Rate 1-10'))
    
    addlcomments = models.TextField(verbose_name=_('Additional Comments'))

    submit_date = models.DateTimeField(
        auto_now_add=True, db_index=True,
        verbose_name=_('Date time submitted')
    )

    class Meta:
        get_latest_by = 'submit_date'
        ordering = ('-submit_date',)
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')

    def __str__(self):
        return self.addlcomments

    @method_event(
        event_manager_class=EventManagerMethodAfter,
        event=event_document_review_deleted,
        target='document',
    )
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            viewname='reviews:review_details', kwargs={
                'review_id': self.pk
            }
        )

    def get_user_label(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        else:
            return self.user.username
    get_user_label.short_description = _('User')

    @method_event(
        event_manager_class=EventManagerSave,
        created={
            'event': event_document_review_created,
            'actor': 'user',
            'action_object': 'document',
            'target': 'self',
        },
        edited={
            'event': event_document_review_edited,
            'action_object': 'document',
            'target': 'self',
        }
    )
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
