from django.conf.urls import url

from .api_views import APIReviewListView, APIReviewView
from .views import (
    DocumentReviewCreateView, DocumentReviewDeleteView,
    DocumentReviewDetailView, DocumentReviewEditView,
    DocumentReviewListView
)

urlpatterns = [
    url(
        regex=r'^documents/(?P<document_id>\d+)/reviews/$',
        name='reviews_for_document', view=DocumentReviewListView.as_view()
    ),
    url(
        regex=r'^documents/(?P<document_id>\d+)/reviews/add/$',
        name='review_add', view=DocumentReviewCreateView.as_view()
    ),
    url(
        regex=r'^reviews/(?P<review_id>\d+)/delete/$',
        name='review_delete', view=DocumentReviewDeleteView.as_view()
    ),
    url(
        regex=r'^reviews/(?P<review_id>\d+)/$', name='review_details',
        view=DocumentReviewDetailView.as_view()
    ),
    url(
        regex=r'^reviews/(?P<review_id>\d+)/edit/$', name='review_edit',
        view=DocumentReviewEditView.as_view()
    ),
]

api_urls = [
    url(
        regex=r'^documents/(?P<document_id>[0-9]+)/reviews/$',
        name='review-list', view=APIReviewListView.as_view()
    ),
    url(
        regex=r'^documents/(?P<document_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/$',
        name='review-detail', view=APIReviewView.as_view()
    ),
]
