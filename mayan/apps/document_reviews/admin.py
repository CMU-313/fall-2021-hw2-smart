from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    date_hierarchy = 'submit_date'
    list_display = ('document', 'submit_date', 'user', 'addlcomments')
    list_filter = ('user',)
    readonly_fields = ('document', 'submit_date', 'user', 'addlcomments')
    search_fields = ('addlcomments',)
