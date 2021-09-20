from mayan.apps.documents.tests.base import GenericDocumentViewTestCase

from .mixins import DocumentReviewTestMixin


class DocumentReviewModelTestCase(
    DocumentReviewTestMixin, GenericDocumentViewTestCase
):
    auto_upload_test_document = False

    def setUp(self):
        super().setUp()
        self._create_test_user()
        self._create_test_document_stub()

    def test_method_get_absolute_url(self):
        self._create_test_review()

        self.assertTrue(self.test_document_review.get_absolute_url())
