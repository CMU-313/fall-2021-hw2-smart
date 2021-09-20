from django.utils.translation import ugettext_lazy as _

from mayan.apps.permissions import PermissionNamespace

namespace = PermissionNamespace(label=_('Reviews'), name='reviews')

permission_document_review_create = namespace.add_permission(
    label=_('Create new reviews'), name='review_create'
)
permission_document_review_delete = namespace.add_permission(
    label=_('Delete reviews'), name='review_delete'
)
permission_document_review_edit = namespace.add_permission(
    label=_('Edit reviews'), name='review_edit'
)
permission_document_review_view = namespace.add_permission(
    label=_('View reviews'), name='review_view'
)
