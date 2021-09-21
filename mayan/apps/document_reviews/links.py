from django.utils.translation import ugettext_lazy as _

from mayan.apps.navigation.classes import Link

from .icons import (
    icon_review_add, icon_review_delete, icon_review_edit,
    icon_reviews_for_document
)
from .permissions import (
    permission_document_review_create, permission_document_review_delete,
    permission_document_review_edit, permission_document_review_view
)

link_review_add = Link(
    args='object.pk', icon=icon_review_add,
    permissions=(permission_document_review_create,), text=_('Add review'),
    view='reviews:review_add',
)
link_review_delete = Link(
    args='object.pk', icon=icon_review_delete,
    permissions=(permission_document_review_delete,), tags='dangerous',
    text=_('Delete'), view='reviews:review_delete',
)
link_review_edit = Link(
    args='object.pk', icon=icon_review_edit,
    permissions=(permission_document_review_edit,),
    text=_('Edit'), view='reviews:review_edit',
)
link_reviews_for_document = Link(
    args='resolved_object.pk', icon=icon_reviews_for_document,
    permissions=(permission_document_review_view,), text=_('Reviews'),
    view='reviews:reviews_for_document',
)
