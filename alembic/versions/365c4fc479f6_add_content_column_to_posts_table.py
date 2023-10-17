"""add content column to posts table

Revision ID: 365c4fc479f6
Revises: e1bcb14d3892
Create Date: 2023-10-17 11:16:19.261544

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '365c4fc479f6'
down_revision: Union[str, None] = 'e1bcb14d3892'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
