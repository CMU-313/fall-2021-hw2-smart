from django.utils.translation import ugettext_lazy as _

from mayan.apps.documents.search import (
    document_file_search, document_file_page_search, document_search,
    document_version_search, document_version_page_search
)

# Document

document_search.add_model_field(
    field='reviews__text', label=_('Reviews')
)

# Document file

document_file_search.add_model_field(
    field='document__reviews__text',
    label=_('Document reviews')
)

# Document file page

document_file_page_search.add_model_field(
    field='document_file__document__reviews__text',
    label=_('Document reviews')
)

# Document version

document_version_search.add_model_field(
    field='document__reviews__text',
    label=_('Document reviews')
)

# Document version page

document_version_page_search.add_model_field(
    field='document_version__document__reviews__text',
    label=_('Document reviews')
)
