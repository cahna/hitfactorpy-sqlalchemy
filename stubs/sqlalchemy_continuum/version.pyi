from .reverter import Reverter as Reverter
from .utils import get_versioning_manager as get_versioning_manager, is_internal_column as is_internal_column, parent_class as parent_class

class VersionClassBase:
    @property
    def previous(self): ...
    @property
    def next(self): ...
    @property
    def index(self): ...
    @property
    def changeset(self): ...
    def revert(self, relations=...): ...