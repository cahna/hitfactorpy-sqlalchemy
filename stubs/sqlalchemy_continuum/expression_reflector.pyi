import sqlalchemy as sa
from .utils import version_table as version_table
from _typeshed import Incomplete

class VersionExpressionReflector(sa.sql.visitors.ReplacingCloningVisitor):
    parent: Incomplete
    relationship: Incomplete
    def __init__(self, parent, relationship) -> None: ...
    def replace(self, column): ...
    def __call__(self, expr): ...
