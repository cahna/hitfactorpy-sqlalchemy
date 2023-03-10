from _typeshed import Incomplete
from sqlalchemy_continuum.plugins import PropertyModTrackerPlugin as PropertyModTrackerPlugin

trigger_sql: str
upsert_cte_sql: str
temporary_transaction_sql: str
insert_temporary_transaction_sql: str
temp_transaction_trigger_sql: str
procedure_sql: str
validity_sql: str

def uses_property_mod_tracking(manager): ...

class SQLConstruct:
    update_validity_for_tables: Incomplete
    operation_type_column_name: Incomplete
    transaction_column_name: Incomplete
    end_transaction_column_name: Incomplete
    version_table_name_format: Incomplete
    use_property_mod_tracking: Incomplete
    table: Incomplete
    excluded_columns: Incomplete
    def __init__(self, table, transaction_column_name, operation_type_column_name, version_table_name_format, excluded_columns: Incomplete | None = ..., update_validity_for_tables: Incomplete | None = ..., use_property_mod_tracking: bool = ..., end_transaction_column_name: Incomplete | None = ...) -> None: ...
    @property
    def table_name(self): ...
    @property
    def transaction_table_name(self): ...
    @property
    def temporary_transaction_table_name(self): ...
    @property
    def version_table_name(self): ...
    @classmethod
    def for_manager(self, manager, cls): ...
    @property
    def columns(self): ...
    @property
    def columns_without_pks(self): ...
    @property
    def pk_columns(self): ...
    def copy_args(self): ...

class UpsertSQL(SQLConstruct):
    builders: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def build_column_names(self): ...
    def build_primary_key_criteria(self): ...
    def build_update_values(self): ...
    def build_insert_values(self): ...
    def build_values(self): ...
    def build_mod_tracking_values(self): ...

class DeleteUpsertSQL(UpsertSQL):
    operation_type: int
    def build_primary_key_criteria(self): ...
    def build_mod_tracking_values(self): ...
    def build_update_values(self): ...
    def build_values(self): ...

class InsertUpsertSQL(UpsertSQL):
    operation_type: int
    def build_mod_tracking_values(self): ...

class UpdateUpsertSQL(UpsertSQL):
    operation_type: int
    def build_mod_tracking_values(self): ...

class ValiditySQL(SQLConstruct):
    @property
    def primary_key_criteria(self): ...

class InsertValiditySQL(ValiditySQL): ...
class UpdateValiditySQL(ValiditySQL): ...

class DeleteValiditySQL(ValiditySQL):
    @property
    def primary_key_criteria(self): ...

def get_validity_sql(class_, tables, params): ...

class CreateTriggerSQL(SQLConstruct): ...

class TransactionSQLConstruct:
    def __init__(self, **kwargs) -> None: ...

class CreateTemporaryTransactionTableSQL(TransactionSQLConstruct):
    table_name: str

class InsertTemporaryTransactionSQL(TransactionSQLConstruct):
    table_name: str
    transaction_values: str

class CreateTriggerFunctionSQL(SQLConstruct): ...

class TransactionTriggerSQL:
    table: Incomplete
    def __init__(self, tx_class) -> None: ...
    @property
    def transaction_table_name(self): ...

def create_versioning_trigger_listeners(manager, cls) -> None: ...
def sync_trigger(conn, table_name, **kwargs) -> None: ...
def create_trigger(conn, table, transaction_column_name: str = ..., operation_type_column_name: str = ..., version_table_name_format: str = ..., excluded_columns: Incomplete | None = ..., use_property_mod_tracking: bool = ..., end_transaction_column_name: Incomplete | None = ...) -> None: ...
def drop_trigger(conn, table_name) -> None: ...
