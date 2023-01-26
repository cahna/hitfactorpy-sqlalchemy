from ..factory import ModelFactory as ModelFactory
from ..utils import version_class as version_class, version_obj as version_obj
from .base import Plugin as Plugin
from _typeshed import Incomplete

class ActivityBase:
    id: Incomplete
    verb: Incomplete
    def actor(self): ...

class ActivityFactory(ModelFactory):
    model_name: str
    object_tx_id: Incomplete
    target_tx_id: Incomplete
    def create_class(self, manager): ...

class ActivityPlugin(Plugin):
    activity_cls: Incomplete
    def after_build_models(self, manager) -> None: ...
    def is_session_modified(self, session): ...
    def before_flush(self, uow, session) -> None: ...
    def after_version_class_built(self, parent_cls, version_cls) -> None: ...
