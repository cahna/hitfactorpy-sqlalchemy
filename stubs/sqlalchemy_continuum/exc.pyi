class VersioningError(Exception): ...
class ClassNotVersioned(VersioningError): ...
class ImproperlyConfigured(VersioningError): ...
