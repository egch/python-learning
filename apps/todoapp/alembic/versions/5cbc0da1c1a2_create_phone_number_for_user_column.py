"""Create phone number for user column

Revision ID: 5cbc0da1c1a2
Revises: 
Create Date: 2026-04-12 15:58:02.050098

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5cbc0da1c1a2'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))



def downgrade() -> None:
    """Downgrade schema."""
    pass
