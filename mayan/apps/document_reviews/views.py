from django.template import RequestContext
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from mayan.apps.documents.models import Document
from mayan.apps.views.generics import (
    SingleObjectCreateView, SingleObjectDeleteView, SingleObjectDetailView,
    SingleObjectEditView, SingleObjectListView
)
from mayan.apps.views.mixins import ExternalObjectViewMixin

from .forms import DocumentReviewDetailForm
from .icons import icon_reviews_for_document
from .links import link_review_add
from .models import Review
from .permissions import (
    permission_document_review_create, permission_document_review_delete,
    permission_document_review_edit, permission_document_review_view
)


class DocumentReviewCreateView(ExternalObjectViewMixin, SingleObjectCreateView):
    external_object_permission = permission_document_review_create
    external_object_pk_url_kwarg = 'document_id'
    external_object_queryset = Document.valid
    fields = ('addlcomments',)

    def get_extra_context(self):
        return {
            'object': self.external_object,
            'title': _('Add review to document: %s') % self.external_object,
        }

    def get_instance_extra_data(self):
        return {
            'document': self.external_object, 'user': self.request.user,
        }

    def get_post_action_redirect(self):
        return reverse(
            viewname='reviews:reviews_for_document', kwargs={
                'document_id': self.kwargs['document_id']
            }
        )

    def get_queryset(self):
        return self.external_object.reviews.all()


class DocumentReviewDeleteView(SingleObjectDeleteView):
    object_permission = permission_document_review_delete
    pk_url_kwarg = 'review_id'

    def get_extra_context(self):
        return {
            'review': self.object,
            'document': self.object.document,
            'navigation_object_list': ('document', 'review'),
            'title': _('Delete review: %s?') % self.object,
        }

    def get_instance_extra_data(self):
        return {
            '_event_actor': self.request.user,
        }

    def get_post_action_redirect(self):
        return reverse(
            viewname='reviews:reviews_for_document', kwargs={
                'document_id': self.object.document_id
            }
        )

    def get_source_queryset(self):
        return Review.objects.filter(
            document_id__in=Document.valid.values('id')
        )


class DocumentReviewDetailView(SingleObjectDetailView):
    form_class = DocumentReviewDetailForm
    pk_url_kwarg = 'review_id'
    object_permission = permission_document_review_view

    def get_extra_context(self):
        return {
            'review': self.object,
            'document': self.object.document,
            'navigation_object_list': ('document', 'review'),
            'title': _('Details for review: %s?') % self.object,
        }

    def get_source_queryset(self):
        return Review.objects.filter(
            document_id__in=Document.valid.values('id')
        )


class DocumentReviewEditView(SingleObjectEditView):
    fields = ('addlcomments',)
    pk_url_kwarg = 'review_id'
    object_permission = permission_document_review_edit

    def get_extra_context(self):
        return {
            'review': self.object,
            'document': self.object.document,
            'navigation_object_list': ('document', 'review'),
            'title': _('Edit review: %s?') % self.object,
        }

    def get_instance_extra_data(self):
        return {
            '_event_actor': self.request.user,
        }

    def get_post_action_redirect(self):
        return reverse(
            viewname='reviews:reviews_for_document', kwargs={
                'document_id': self.object.document_id
            }
        )

    def get_source_queryset(self):
        return Review.objects.filter(
            document_id__in=Document.valid.values('id')
        )


class DocumentReviewListView(ExternalObjectViewMixin, SingleObjectListView):
    external_object_permission = permission_document_review_view
    external_object_pk_url_kwarg = 'document_id'
    external_object_queryset = Document.valid

    def get_extra_context(self):
        return {
            'hide_link': True,
            'hide_object': True,
            'no_results_icon': icon_reviews_for_document,
            'no_results_external_link': link_review_add.resolve(
                RequestContext(self.request, {'object': self.external_object})
            ),
            'no_results_text': _(
                'Document reviews score a student based on different factors.'
            ),
            'no_results_title': _('There are no reviews'),
            'object': self.external_object,
            'title': _('Reviews for document: %s') % self.external_object,
        }

    def get_source_queryset(self):
        return self.external_object.reviews.all()
