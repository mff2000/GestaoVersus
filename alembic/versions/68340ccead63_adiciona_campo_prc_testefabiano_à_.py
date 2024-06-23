"""Adiciona campo PRC_TESTEFABIANO à tabela Prc_Cad

Revision ID: 68340ccead63
Revises: 1b9d99dd13d1
Create Date: 2024-06-23 14:16:00.817309

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '68340ccead63'
down_revision = '1b9d99dd13d1'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.add_column('Prc_Cad', sa.Column('PRC_TESTEFABIANO', sa.String(length=999), nullable=True))

def downgrade() -> None:
    op.drop_column('Prc_Cad', 'PRC_TESTEFABIANO')
