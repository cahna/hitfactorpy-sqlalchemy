from .operation import Operations as Operations
from .utils import end_tx_column_name as end_tx_column_name, is_session_modified as is_session_modified, tx_column_name as tx_column_name, version_class as version_class, versioned_column_properties as versioned_column_properties
from _typeshed import Incomplete

class UnitOfWork:
    manager: Incomplete
    def __init__(self, manager) -> None: ...
    version_session: Incomplete
    current_transaction: Incomplete
    operations: Incomplete
    pending_statements: Incomplete
    version_objs: Incomplete
    def reset(self, session: Incomplete | None = ...) -> None: ...
    def is_modified(self, session): ...
    def process_before_flush(self, session) -> None: ...
    def process_after_flush(self, session) -> None: ...
    def transaction_args(self, session): ...
    def create_transaction(self, session): ...
    def get_or_create_version_object(self, target): ...
    def process_operation(self, operation) -> None: ...
    def create_version_objects(self, session) -> None: ...
    def version_validity_subquery(self, parent, version_obj, alias: Incomplete | None = ...): ...
    def update_version_validity(self, parent, version_obj) -> None: ...
    def create_association_versions(self, session) -> None: ...
    def make_versions(self, session) -> None: ...
    @property
    def has_changes(self): ...
    def assign_attributes(self, parent_obj, version_obj) -> None: ...