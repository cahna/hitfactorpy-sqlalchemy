from _typeshed import Incomplete

class Operation:
    INSERT: int
    UPDATE: int
    DELETE: int
    target: Incomplete
    type: Incomplete
    processed: bool
    def __init__(self, target, type) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class Operations:
    objects: Incomplete
    def __init__(self) -> None: ...
    def format_key(self, target): ...
    def __contains__(self, target) -> bool: ...
    def __setitem__(self, key, operation) -> None: ...
    def __getitem__(self, key): ...
    def __delitem__(self, key) -> None: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self): ...
    @property
    def entities(self): ...
    def iteritems(self): ...
    def items(self): ...
    def add(self, operation) -> None: ...
    def add_insert(self, target) -> None: ...
    def add_update(self, target) -> None: ...
    def add_delete(self, target) -> None: ...
