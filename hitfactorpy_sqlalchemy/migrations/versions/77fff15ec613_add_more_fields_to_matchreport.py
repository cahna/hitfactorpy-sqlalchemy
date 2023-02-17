"""add more fields to MatchReport

Revision ID: 77fff15ec613
Revises: ffb9404a7bbf
Create Date: 2023-02-17 12:58:25.745603

"""  # noqa: W291
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "77fff15ec613"
down_revision = "ffb9404a7bbf"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("match_report", sa.Column("platform", sa.Unicode(), nullable=True))
    op.add_column("match_report", sa.Column("ps_product", sa.Unicode(), nullable=True))
    op.add_column("match_report", sa.Column("ps_version", sa.Unicode(), nullable=True))
    op.add_column("match_report", sa.Column("club_name", sa.Unicode(), nullable=True))
    op.add_column("match_report", sa.Column("club_code", sa.Unicode(), nullable=True))

    op.add_column("match_report_version", sa.Column("platform", sa.Unicode(), autoincrement=False, nullable=True))
    op.add_column("match_report_version", sa.Column("ps_product", sa.Unicode(), autoincrement=False, nullable=True))
    op.add_column("match_report_version", sa.Column("ps_version", sa.Unicode(), autoincrement=False, nullable=True))
    op.add_column("match_report_version", sa.Column("club_name", sa.Unicode(), autoincrement=False, nullable=True))
    op.add_column("match_report_version", sa.Column("club_code", sa.Unicode(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("match_report_version", "club_code")
    op.drop_column("match_report_version", "club_name")
    op.drop_column("match_report_version", "ps_version")
    op.drop_column("match_report_version", "ps_product")
    op.drop_column("match_report_version", "platform")

    op.drop_column("match_report", "club_code")
    op.drop_column("match_report", "club_name")
    op.drop_column("match_report", "ps_version")
    op.drop_column("match_report", "ps_product")
    op.drop_column("match_report", "platform")
    # ### end Alembic commands ###
