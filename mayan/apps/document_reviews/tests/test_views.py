from mayan.apps.documents.tests.base import GenericDocumentViewTestCase

from ..events import (
    event_document_review_created, event_document_review_deleted,
    event_document_review_edited
)
from ..models import Review
from ..permissions import (
    permission_document_review_create, permission_document_review_delete,
    permission_document_review_edit, permission_document_review_view
)

from .mixins import DocumentReviewTestMixin, DocumentReviewViewTestMixin


class DocumentReviewViewTestCase(
    DocumentReviewViewTestMixin, DocumentReviewTestMixin,
    GenericDocumentViewTestCase
):
    auto_upload_test_document = False

    def setUp(self):
        super().setUp()
        self._create_test_user()
        self._create_test_document_stub()

    def test_review_create_view_no_permission(self):
        review_count = Review.objects.count()

        self._clear_events()

        response = self._request_test_review_create_view()
        self.assertEqual(response.status_code, 404)

        self.assertEqual(Review.objects.count(), review_count)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_review_create_view_with_permissions(self):
        review_count = Review.objects.count()

        self.grant_access(
            obj=self.test_document,
            permission=permission_document_review_create
        )

        self._clear_events()

        response = self._request_test_review_create_view()
        self.assertEqual(response.status_code, 302)

        self.assertEqual(Review.objects.count(), review_count + 1)

        events = self._get_test_events()
        self.assertEqual(events.count(), 1)

        self.assertEqual(events[0].action_object, self.test_document)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, self.test_document_review)
        self.assertEqual(events[0].verb, event_document_review_created.id)

    def test_trashed_document_review_create_view_with_permissions(self):
        review_count = Review.objects.count()

        self.grant_access(
            obj=self.test_document,
            permission=permission_document_review_create
        )

        self.test_document.delete()

        self._clear_events()

        response = self._request_test_review_create_view()
        self.assertEqual(response.status_code, 404)

        self.assertEqual(Review.objects.count(), review_count)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_review_delete_view_no_permission(self):
        self._create_test_review()

        review_count = Review.objects.count()

        self._clear_events()

        response = self._request_test_review_delete_view()
        self.assertEqual(response.status_code, 404)

        self.assertEqual(Review.objects.count(), review_count)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_review_delete_view_with_access(self):
        self._create_test_review()

        self.grant_access(
            obj=self.test_document,
            permission=permission_document_review_delete
        )

        review_count = Review.objects.count()

        self._clear_events()

        response = self._request_test_review_delete_view()
        self.assertEqual(response.status_code, 302)

        self.assertEqual(Review.objects.count(), review_count - 1)

        events = self._get_test_events()
        self.assertEqual(events.count(), 1)

        self.assertEqual(events[0].action_object, None)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, self.test_document)
        self.assertEqual(events[0].verb, event_document_review_deleted.id)

    def test_trashed_document_review_delete_view_with_access(self):
        self._create_test_review()

        self.grant_access(
            obj=self.test_document,
            permission=permission_document_review_delete
        )

        self.test_document.delete()

        review_count = Review.objects.count()

        self._clear_events()

        response = self._request_test_review_delete_view()
        self.assertEqual(response.status_code, 404)

        self.assertEqual(Review.objects.count(), review_count)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_review_detail_view_no_permission(self):
        self._create_test_review()

        self._clear_events()

        response = self._request_test_review_detail_view()
        self.assertEqual(response.status_code, 404)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_review_detail_view_with_access(self):
        self._create_test_review()

        self.grant_access(
            obj=self.test_document,
            permission=permission_document_review_view
        )

        self._clear_events()

        response = self._request_test_review_detail_view()
        self.assertContains(
            response=response, text=self.test_document_review.text,
            status_code=200
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_trashed_documen_review_detail_view_with_access(self):
        self._create_test_review()

        self.grant_access(
            obj=self.test_document,
            permission=permission_document_review_view
        )

        self.test_document.delete()

        self._clear_events()

        response = self._request_test_review_detail_view()
        self.assertEqual(response.status_code, 404)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_review_edit_view_no_permission(self):
        self._create_test_review()

        review_text = self.test_document_review.text

        self._clear_events()

        response = self._request_test_review_edit_view()
        self.assertEqual(response.status_code, 404)

        self.test_document_review.refresh_from_db()
        self.assertEqual(self.test_document_review.text, review_text)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_review_edit_view_with_access(self):
        self._create_test_review()

        self.grant_access(
            obj=self.test_document, permission=permission_document_review_edit
        )

        review_text = self.test_document_review.text

        self._clear_events()

        response = self._request_test_review_edit_view()
        self.assertEqual(response.status_code, 302)

        self.test_document_review.refresh_from_db()
        self.assertNotEqual(self.test_document_review.text, review_text)

        events = self._get_test_events()
        self.assertEqual(events.count(), 1)

        self.assertEqual(events[0].action_object, self.test_document)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, self.test_document_review)
        self.assertEqual(events[0].verb, event_document_review_edited.id)

    def test_trashed_document_review_edit_view_with_access(self):
        self._create_test_review()

        self.grant_access(
            obj=self.test_document, permission=permission_document_review_edit
        )

        review_text = self.test_document_review.text

        self.test_document.delete()

        self._clear_events()

        response = self._request_test_review_edit_view()
        self.assertEqual(response.status_code, 404)

        self.test_document_review.refresh_from_db()
        self.assertEqual(self.test_document_review.text, review_text)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_review_list_view_with_no_permission(self):
        self._create_test_review()

        self._clear_events()

        response = self._request_test_review_list_view()
        self.assertNotContains(
            response=response, text=self.test_document_review.text,
            status_code=404
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_review_list_view_with_access(self):
        self._create_test_review()

        self.grant_access(
            obj=self.test_document,
            permission=permission_document_review_view
        )

        self._clear_events()

        response = self._request_test_review_list_view()
        self.assertContains(
            response=response, text=self.test_document_review.text,
            status_code=200
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_trashed_document_review_list_view_with_access(self):
        self._create_test_review()

        self.grant_access(
            obj=self.test_document,
            permission=permission_document_review_view
        )

        self.test_document.delete()

        self._clear_events()

        response = self._request_test_review_list_view()
        self.assertEqual(response.status_code, 404)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)
