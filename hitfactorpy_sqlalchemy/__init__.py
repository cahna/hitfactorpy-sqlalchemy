from importlib.metadata import version
from os import path
from pathlib import Path

__version__ = version("hitfactorpy_sqlalchemy")
MODULE_PATH = Path(path.dirname(path.abspath(__file__)))
