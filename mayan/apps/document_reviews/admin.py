from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    date_hierarchy = 'submit_date'
    list_display = ('document', 'submit_date', 'user', 'firstName', 'lastName', 'gradYear', 'fieldOfStudy', 'gpaScale', 'technicalScale', 'communicationScale', 'experienceScale', 'addlcomments')
    list_filter = ('user',)
    readonly_fields = ('document', 'submit_date', 'user', 'firstName', 'lastName', 'gradYear', 'fieldOfStudy', 'gpaScale', 'technicalScale', 'communicationScale', 'experienceScale', 'addlcomments')
    search_fields = ('addlcomments',)
