"""create phone number

Revision ID: 7cb321c95531
Revises: 
Create Date: 2025-09-22 16:07:59.763183

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7cb321c95531'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')

