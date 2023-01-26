from .exc import ClassNotVersioned as ClassNotVersioned, ImproperlyConfigured as ImproperlyConfigured
from .operation import Operation as Operation
from .transaction import TransactionFactory as TransactionFactory
from .unit_of_work import UnitOfWork as UnitOfWork
from .utils import changeset as changeset, count_versions as count_versions, get_versioning_manager as get_versioning_manager, is_modified as is_modified, is_session_modified as is_session_modified, parent_class as parent_class, transaction_class as transaction_class, tx_column_name as tx_column_name, vacuum as vacuum, version_class as version_class
from _typeshed import Incomplete

versioning_manager: Incomplete

def make_versioned(mapper=..., session=..., manager=..., plugins: Incomplete | None = ..., options: Incomplete | None = ..., user_cls: str | None = ...) -> None: ...
def remove_versioning(mapper=..., session=..., manager=...) -> None: ...
