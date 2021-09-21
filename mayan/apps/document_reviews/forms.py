from django import forms

from mayan.apps.views.forms import DetailForm

from .models import Review


class DocumentReviewDetailForm(DetailForm):

    class Meta:
        fields = ('addlcomments',)
        extra_fields = (
            {'field': 'submit_date', 'widget': forms.widgets.DateTimeInput},
            {'field': 'user'},
        )
        model = Review
