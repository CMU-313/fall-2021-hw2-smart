from django.apps import apps
from django.utils.translation import ugettext_lazy as _

from mayan.apps.acls.classes import ModelPermission
from mayan.apps.common.apps import MayanAppConfig
from mayan.apps.common.menus import menu_facet, menu_object, menu_secondary
from mayan.apps.events.classes import EventModelRegistry, ModelEventType
from mayan.apps.events.permissions import permission_events_view
from mayan.apps.navigation.classes import SourceColumn

from .events import (
    event_document_review_created, event_document_review_deleted,
    event_document_review_edited
)
from .links import (
    link_review_add, link_review_delete, link_review_edit,
    link_reviews_for_document
)
from .permissions import (
    permission_document_review_create, permission_document_review_delete,
    permission_document_review_edit, permission_document_review_view
)


class DocumentReviewsApp(MayanAppConfig):
    app_namespace = 'reviews'
    app_url = 'reviews'
    has_rest_api = True
    has_tests = True
    name = 'mayan.apps.document_reviews'
    verbose_name = _('Document reviews')

    def ready(self):
        super().ready()

        Document = apps.get_model(
            app_label='documents', model_name='Document'
        )

        Review = self.get_model(model_name='Review')

        EventModelRegistry.register(model=Review)

        ModelEventType.register(
            model=Review, event_types=(
                event_document_review_edited,
            )
        )
        ModelEventType.register(
            model=Document, event_types=(
                event_document_review_created, event_document_review_deleted,
                event_document_review_edited
            )
        )

        ModelPermission.register(
            model=Review, permissions=(permission_events_view,)
        )
        ModelPermission.register_inheritance(
            model=Review, related='document',
        )
        ModelPermission.register(
            model=Document, permissions=(
                permission_document_review_create,
                permission_document_review_delete,
                permission_document_review_edit,
                permission_document_review_view
            )
        )

        SourceColumn(
            attribute='submit_date', is_identifier=True, is_sortable=True,
            source=Review
        )
        SourceColumn(
            attribute='get_user_label', is_sortable=True,
            include_label=True, sort_field='user', source=Review
        )
        SourceColumn(attribute='text', include_label=True, source=Review)

        menu_facet.bind_links(
            links=(link_reviews_for_document,), sources=(Document,)
        )

        menu_secondary.bind_links(
            links=(link_review_add,),
            sources=(
                'reviews:reviews_for_document', 'reviews:review_add',
                'reviews:review_delete', 'reviews:review_details',
                'reviews:review_edit', 'reviews:review_multiple_delete'
            )
        )

        menu_object.bind_links(
            links=(link_review_delete, link_review_edit), sources=(Review,)
        )
