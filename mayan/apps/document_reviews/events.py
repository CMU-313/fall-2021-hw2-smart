from django.utils.translation import ugettext_lazy as _

from mayan.apps.events.classes import EventTypeNamespace

namespace = EventTypeNamespace(
    label=_('Document reviews'), name='document_reviews'
)

event_document_review_created = namespace.add_event_type(
    label=_('Document review created'), name='create'
)
event_document_review_deleted = namespace.add_event_type(
    label=_('Document review deleted'), name='delete'
)
event_document_review_edited = namespace.add_event_type(
    label=_('Document review edited'), name='edited'
)
