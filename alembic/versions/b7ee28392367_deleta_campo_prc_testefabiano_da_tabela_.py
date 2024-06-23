"""Deleta campo PRC_TESTEFABIANO da tabela Prc_Cad

Revision ID: b7ee28392367
Revises: 68340ccead63
Create Date: 2024-06-23 14:29:46.527798

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b7ee28392367'
down_revision = '68340ccead63'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.drop_column('Prc_Cad', 'PRC_TESTEFABIANO')  # Remove a coluna PRC_TESTEFABIANO

def downgrade() -> None:
    op.add_column('Prc_Cad', sa.Column('PRC_TESTEFABIANO', sa.String(length=999), nullable=True))  # Adiciona a coluna de volta em caso de downgrade
