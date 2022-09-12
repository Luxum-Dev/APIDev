"""create post table

Revision ID: 7a6911621276
Revises: 
Create Date: 2022-09-11 21:40:47.030956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a6911621276'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column(
        "id", sa.Integer(), nullable=False, primary_key=True), sa.Column("title", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_table("posts")
    pass
