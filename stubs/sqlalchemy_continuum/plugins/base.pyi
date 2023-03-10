from _typeshed import Incomplete

class Plugin:
    def is_session_modified(self, session): ...
    def after_build_tx_class(self, manager) -> None: ...
    def after_build_models(self, manager) -> None: ...
    def after_build_version_table_columns(self, table_builder, columns) -> None: ...
    def before_flush(self, uow, session) -> None: ...
    def before_create_version_objects(self, uow, session) -> None: ...
    def after_create_version_objects(self, uow, session) -> None: ...
    def after_create_version_object(self, uow, parent_obj, version_obj) -> None: ...
    def transaction_args(self, uow, session): ...
    def after_version_class_built(self, parent_cls, version_cls) -> None: ...
    def after_construct_changeset(self, version_obj, changeset) -> None: ...

class PluginCollection:
    plugins: Incomplete
    def __init__(self, plugins: Incomplete | None = ...) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __getitem__(self, index): ...
    def __setitem__(self, index, element) -> None: ...
    def __delitem__(self, index) -> None: ...
    def __getattr__(self, attr): ...
    def append(self, el) -> None: ...
