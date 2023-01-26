from .dialects.postgresql import CreateTemporaryTransactionTableSQL as CreateTemporaryTransactionTableSQL, InsertTemporaryTransactionSQL as InsertTemporaryTransactionSQL, TransactionTriggerSQL as TransactionTriggerSQL
from .exc import ImproperlyConfigured as ImproperlyConfigured
from .factory import ModelFactory as ModelFactory
from _typeshed import Incomplete
from functools import partial as partial

def compile_big_integer(element, compiler, **kw): ...

class NoChangesAttribute(Exception): ...

class TransactionBase:
    issued_at: Incomplete
    @property
    def entity_names(self): ...
    @property
    def changed_entities(self): ...

procedure_sql: str

def create_triggers(cls) -> None: ...

class TransactionFactory(ModelFactory):
    model_name: str
    remote_addr: Incomplete
    def __init__(self, remote_addr: bool = ...) -> None: ...
    def create_class(self, manager): ...
