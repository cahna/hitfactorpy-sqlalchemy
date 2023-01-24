from ..factory import ModelFactory as ModelFactory
from .base import Plugin as Plugin
from _typeshed import Incomplete

class TransactionMetaBase:
    transaction_id: Incomplete
    key: Incomplete
    value: Incomplete

class TransactionMetaFactory(ModelFactory):
    model_name: str
    def create_class(self, manager): ...

class TransactionMetaPlugin(Plugin):
    model_class: Incomplete
    def after_build_tx_class(self, manager) -> None: ...
    def after_build_models(self, manager) -> None: ...
