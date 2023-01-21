from typing import Any, Dict

import sqlalchemy as sa
from hitfactorpy.enums import Classification, Division, MatchLevel, PowerFactor, Scoring
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_continuum import make_versioned

make_versioned(user_cls=None)

"""Base ORM Model"""
BaseModel = declarative_base()


class ModelWithId(BaseModel):  # type: ignore
    """Model with a database-internal id and a public uuid"""

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    uuid = sa.Column(
        UUID(as_uuid=True), nullable=False, unique=True, index=True, server_default=sa.text("gen_random_uuid()")
    )


class VersionedModel(ModelWithId):
    """Model with auto-managed versioning via sqlalchemy-continuum"""

    __versioned__: Dict[Any, Any] = {}


class MatchReportCompetitor(VersionedModel):
    __tablename__ = "match_report_competitor"

    member_number = sa.Column(sa.Unicode(64))
    first_name = sa.Column(sa.Unicode(64))
    last_name = sa.Column(sa.Unicode(64))
    division = sa.Column(Division)
    classification = sa.Column(Classification)
    power_factor = sa.Column(PowerFactor)
    dq = sa.Column(sa.Boolean, nullable=False, default=False)
    reentry = sa.Column(sa.Boolean, nullable=False, default=False)


class MatchReportStage(VersionedModel):
    __tablename__ = "match_report_stage"

    name = sa.Column(sa.Unicode(255))
    min_rounds = sa.Column(sa.Integer, nullable=False)
    max_points = sa.Column(sa.Integer, nullable=False)
    classifier = sa.Column(sa.Boolean, nullable=False, default=False)
    classifier_number = sa.Column(sa.Unicode(64))
    scoring_type = sa.Column(Scoring, nullable=False, default=Scoring.COMSTOCK)


class MatchReportStageScore(VersionedModel):
    __tablename__ = "match_report_stage_score"

    competitor_id = sa.Column(sa.Integer, nullable=False)
    stage_id = sa.Column(sa.Integer, nullable=False)
    a = sa.Column(sa.Integer, nullable=False, default=0)
    b = sa.Column(sa.Integer, nullable=False, default=0)
    c = sa.Column(sa.Integer, nullable=False, default=0)
    d = sa.Column(sa.Integer, nullable=False, default=0)
    m = sa.Column(sa.Integer, nullable=False, default=0)
    npm = sa.Column(sa.Integer, nullable=False, default=0)
    ns = sa.Column(sa.Integer, nullable=False, default=0)
    procedural = sa.Column(sa.Integer, nullable=False, default=0)
    late_shot = sa.Column(sa.Integer, nullable=False, default=0)
    extra_shot = sa.Column(sa.Integer, nullable=False, default=0)
    extra_hit = sa.Column(sa.Integer, nullable=False, default=0)
    other_penalty = sa.Column(sa.Integer, nullable=False, default=0)
    t1 = sa.Column(sa.Float, nullable=False, default=0.0)
    t2 = sa.Column(sa.Float, nullable=False, default=0.0)
    t3 = sa.Column(sa.Float, nullable=False, default=0.0)
    t4 = sa.Column(sa.Float, nullable=False, default=0.0)
    t5 = sa.Column(sa.Float, nullable=False, default=0.0)
    time = sa.Column(sa.Float, nullable=False, default=0.0)
    dq = sa.Column(sa.Boolean, nullable=False, default=False)
    dnf = sa.Column(sa.Boolean, nullable=False, default=False)


class MatchReport(VersionedModel):
    __tablename__ = "match_report"

    name = sa.Column(sa.Unicode(255), nullable=False)
    date = sa.Column(sa.Date)
    match_level = sa.Column(MatchLevel)
