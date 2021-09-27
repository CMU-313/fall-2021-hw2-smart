from rest_framework import serializers
from rest_framework.reverse import reverse

from mayan.apps.documents.serializers.document_serializers import DocumentSerializer
from mayan.apps.user_management.serializers import UserSerializer

from .models import Review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    document = DocumentSerializer(read_only=True)
    document_reviews_url = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        fields = (
            'document', 'document_reviews_url', 'id', 'submit_date', 'firstName', 'lastName', 'gradYear', 'fieldOfStudy', 'gpaScale', 'technicalScale', 'communicationScale', 'experienceScale', 'addlcomments', 'addlreviews', 'url', 'user'
        )
        model = Review

    def get_document_reviews_url(self, instance):
        return reverse(
            viewname='rest_api:review-list', kwargs={
                'document_id': instance.document_id,
            }, request=self.context['request'], format=self.context['format']
        )

    def get_url(self, instance):
        return reverse(
            viewname='rest_api:review-detail', kwargs={
                'document_id': instance.document_id,
                'review_id': instance.pk
            }, request=self.context['request'], format=self.context['format']
        )


class WritableReviewSerializer(serializers.ModelSerializer):
    document = DocumentSerializer(read_only=True)
    document_reviews_url = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        fields = (
            'document', 'document_reviews_url', 'id', 'submit_date', 'firstName', 'lastName', 'gradYear', 'fieldOfStudy', 'gpaScale', 'technicalScale', 'communicationScale', 'experienceScale', 'addlcomments', 'addlreviews', 'url', 'user'
        )
        model = Review
        read_only_fields = ('document',)

    def create(self, validated_data):
        validated_data['document'] = self.context['document']
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_document_reviews_url(self, instance):
        return reverse(
            viewname='rest_api:review-list', kwargs={
                'document_id': instance.document_id,
            }, request=self.context['request'], format=self.context['format']
        )

    def get_url(self, instance):
        return reverse(
            viewname='rest_api:review-detail', kwargs={
                'document_id': instance.document_id,
                'review_id': instance.pk
            }, request=self.context['request'], format=self.context['format']
        )
