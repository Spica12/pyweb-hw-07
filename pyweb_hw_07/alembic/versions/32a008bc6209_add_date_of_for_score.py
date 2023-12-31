"""add_date_of_for_score

Revision ID: 32a008bc6209
Revises: 356a1cc6e40d
Create Date: 2023-12-10 22:24:49.895043

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32a008bc6209'
down_revision: Union[str, None] = '356a1cc6e40d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('scores', sa.Column('data_of', sa.Date(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('scores', 'data_of')
    # ### end Alembic commands ###
