from rest_framework import status

from mayan.apps.documents.tests.mixins.document_mixins import DocumentTestMixin
from mayan.apps.rest_api.tests.base import BaseAPITestCase

from ..events import (
    event_document_review_created, event_document_review_deleted,
    event_document_review_edited
)
from ..models import Review
from ..permissions import (
    permission_document_review_create, permission_document_review_delete,
    permission_document_review_edit, permission_document_review_view
)

from .mixins import ReviewAPIViewTestMixin, DocumentReviewTestMixin


class ReviewAPIViewTestCase(
    ReviewAPIViewTestMixin, DocumentReviewTestMixin, DocumentTestMixin,
    BaseAPITestCase
):
    auto_upload_test_document = False

    def setUp(self):
        super().setUp()
        self._create_test_user()
        self._create_test_document_stub()

    def test_review_create_api_view_no_permission(self):
        self._clear_events()

        response = self._request_test_review_create_api_view()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.assertEqual(Review.objects.count(), 0)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_review_create_api_view_with_access(self):
        self.grant_access(
            obj=self.test_document, permission=permission_document_review_create
        )

        self._clear_events()

        response = self._request_test_review_create_api_view()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        review = Review.objects.first()
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(response.data['id'], review.pk)

        events = self._get_test_events()
        self.assertEqual(events.count(), 1)

        self.assertEqual(events[0].action_object, self.test_document)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, self.test_document_review)
        self.assertEqual(events[0].verb, event_document_review_created.id)

    def test_review_delete_api_view_no_permission(self):
        self._create_test_review()

        self._clear_events()

        response = self._request_test_review_delete_api_view()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.assertTrue(self.test_document_review in Review.objects.all())

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_review_delete_api_view_with_access(self):
        self._create_test_review()
        self.grant_access(
            obj=self.test_document, permission=permission_document_review_delete
        )

        self._clear_events()

        response = self._request_test_review_delete_api_view()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(self.test_document_review in Review.objects.all())

        events = self._get_test_events()
        self.assertEqual(events.count(), 1)

        self.assertEqual(events[0].action_object, None)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, self.test_document)
        self.assertEqual(events[0].verb, event_document_review_deleted.id)

    def test_review_detail_api_view_no_permission(self):
        self._create_test_review()

        self._clear_events()

        response = self._request_test_review_detail_api_view()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_review_detail_api_view_with_access(self):
        self._create_test_review()
        self.grant_access(
            obj=self.test_document, permission=permission_document_review_view
        )

        self._clear_events()

        response = self._request_test_review_detail_api_view()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['text'], self.test_document_review.text)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_review_edit_via_patch_api_view_no_permission(self):
        self._create_test_review()
        review_text = self.test_document_review.text

        self._clear_events()

        response = self._request_test_review_edit_patch_api_view()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.test_document_review.refresh_from_db()
        self.assertEqual(self.test_document_review.text, review_text)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_review_edit_via_patch_api_view_with_access(self):
        self._create_test_review()
        self.grant_access(
            obj=self.test_document, permission=permission_document_review_edit
        )
        review_text = self.test_document_review.text

        self._clear_events()

        response = self._request_test_review_edit_patch_api_view()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.test_document_review.refresh_from_db()
        self.assertNotEqual(self.test_document_review.text, review_text)

        events = self._get_test_events()
        self.assertEqual(events.count(), 1)

        self.assertEqual(events[0].action_object, self.test_document)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, self.test_document_review)
        self.assertEqual(events[0].verb, event_document_review_edited.id)

    def test_review_list_api_view_no_permission(self):
        self._create_test_review()

        self._clear_events()

        response = self._request_test_review_list_api_view()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_review_list_api_view_with_access(self):
        self._create_test_review()
        self.grant_access(
            obj=self.test_document, permission=permission_document_review_view
        )

        self._clear_events()

        response = self._request_test_review_list_api_view()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'][0]['text'], self.test_document_review.text
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)
