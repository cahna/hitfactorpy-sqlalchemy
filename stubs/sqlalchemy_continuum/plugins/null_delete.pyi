from ..operation import Operation as Operation
from ..utils import is_internal_column as is_internal_column, versioned_column_properties as versioned_column_properties
from .base import Plugin as Plugin

class NullDeletePlugin(Plugin):
    def should_nullify_column(self, version_obj, prop): ...
    def after_create_version_object(self, uow, parent_obj, version_obj) -> None: ...
