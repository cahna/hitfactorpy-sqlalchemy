from pathlib import Path

from alembic.config import Config as AlembicConfig

from .defaults import HITFACTORPY_ALEMBIC_DIR, HITFACTORPY_SQLALCHEMY_URL


def HitfactorpyAlembicConfig(
    script_location: str | Path = HITFACTORPY_ALEMBIC_DIR, sqlalchemy_url: str = HITFACTORPY_SQLALCHEMY_URL
) -> AlembicConfig:
    alembic_cfg = AlembicConfig()
    alembic_cfg.set_main_option("script_location", str(script_location))
    alembic_cfg.set_main_option("sqlalchemy.url", sqlalchemy_url)
    return alembic_cfg
