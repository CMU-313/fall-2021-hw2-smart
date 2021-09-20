from django.db.models import Q

from ..models import Review

from .literals import TEST_COMMENT_TEXT, TEST_COMMENT_TEXT_EDITED


class ReviewAPIViewTestMixin:
    def _request_test_review_create_api_view(self):
        pk_list = list(Review.objects.values_list('pk', flat=True))

        response = self.post(
            viewname='rest_api:review-list', kwargs={
                'document_id': self.test_document.pk
            }, data={
                'text': TEST_COMMENT_TEXT
            }
        )

        try:
            self.test_document_review = Review.objects.get(
                ~Q(pk__in=pk_list)
            )
        except Review.DoesNotExist:
            self.test_document_review = None

        return response

    def _request_test_review_delete_api_view(self):
        return self.delete(
            viewname='rest_api:review-detail', kwargs={
                'document_id': self.test_document.pk,
                'review_id': self.test_document_review.pk,
            }
        )

    def _request_test_review_detail_api_view(self):
        return self.get(
            viewname='rest_api:review-detail', kwargs={
                'document_id': self.test_document.pk,
                'review_id': self.test_document_review.pk
            }
        )

    def _request_test_review_edit_patch_api_view(self):
        return self.patch(
            viewname='rest_api:review-detail', kwargs={
                'document_id': self.test_document.pk,
                'review_id': self.test_document_review.pk,
            }, data={'text': TEST_COMMENT_TEXT_EDITED}
        )

    def _request_test_review_list_api_view(self):
        return self.get(
            viewname='rest_api:review-list', kwargs={
                'document_id': self.test_document.pk
            }
        )


class DocumentReviewTestMixin:
    def _create_test_review(self):
        self.test_document_review = self.test_document.reviews.create(
            text=TEST_COMMENT_TEXT, user=self.test_user
        )


class DocumentReviewViewTestMixin:
    def _request_test_review_create_view(self):
        pk_list = list(Review.objects.values_list('pk', flat=True))

        response = self.post(
            viewname='reviews:review_add', kwargs={
                'document_id': self.test_document.pk
            }, data={'text': TEST_COMMENT_TEXT}
        )

        try:
            self.test_document_review = Review.objects.get(
                ~Q(pk__in=pk_list)
            )
        except Review.DoesNotExist:
            self.test_document_review = None

        return response

    def _request_test_review_delete_view(self):
        return self.post(
            viewname='reviews:review_delete', kwargs={
                'review_id': self.test_document_review.pk
            },
        )

    def _request_test_review_detail_view(self):
        return self.get(
            viewname='reviews:review_details', kwargs={
                'review_id': self.test_document_review.pk
            },
        )

    def _request_test_review_edit_view(self):
        return self.post(
            viewname='reviews:review_edit', kwargs={
                'review_id': self.test_document_review.pk,
            }, data={
                'text': TEST_COMMENT_TEXT_EDITED
            }
        )

    def _request_test_review_list_view(self):
        return self.get(
            viewname='reviews:reviews_for_document', kwargs={
                'document_id': self.test_document.pk,
            }
        )
