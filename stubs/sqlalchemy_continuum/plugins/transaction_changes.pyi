from ..factory import ModelFactory as ModelFactory
from ..utils import option as option
from .base import Plugin as Plugin
from _typeshed import Incomplete

class TransactionChangesBase:
    transaction_id: Incomplete
    entity_name: Incomplete

class TransactionChangesFactory(ModelFactory):
    model_name: str
    def create_class(self, manager): ...

class TransactionChangesPlugin(Plugin):
    objects: Incomplete
    model_class: Incomplete
    def after_build_tx_class(self, manager) -> None: ...
    def after_build_models(self, manager) -> None: ...
    def before_create_version_objects(self, uow, session) -> None: ...
    def clear(self) -> None: ...
    def after_rollback(self, uow, session) -> None: ...
    def ater_commit(self, uow, session) -> None: ...
    def after_version_class_built(self, parent_cls, version_cls) -> None: ...