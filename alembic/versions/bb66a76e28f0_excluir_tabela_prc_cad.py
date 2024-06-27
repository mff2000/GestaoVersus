"""excluir_tabela_prc_cad

Revision ID: bb66a76e28f0
Revises: f8997513c8de
Create Date: 2024-06-27 19:57:29.816835

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb66a76e28f0'
down_revision: Union[str, None] = 'f8997513c8de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
