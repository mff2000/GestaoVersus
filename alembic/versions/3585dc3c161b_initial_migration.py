"""Initial migration

Revision ID: 3585dc3c161b
Revises: 
Create Date: 2024-06-20 22:16:49.033980

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3585dc3c161b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Prc_Cad',
    sa.Column('PRC_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('PRC_TIPO', sa.String(length=20), nullable=True),
    sa.Column('PRC_PAI', sa.Integer(), nullable=True),
    sa.Column('PRC_NIVEL', sa.Integer(), nullable=True),
    sa.Column('PRC_CODIGO', sa.String(length=20), nullable=True),
    sa.Column('PRC_NOME', sa.String(length=256), nullable=True),
    sa.Column('PRC_GERENCIAM', sa.String(length=256), nullable=True),
    sa.Column('PRC_MISSAO', sa.String(length=999), nullable=True),
    sa.Column('PRC_DONO_ID', sa.Integer(), nullable=True),
    sa.Column('PRC_EXIG_QUALID', sa.String(length=999), nullable=True),
    sa.Column('PRC_INDICE_ID', sa.Integer(), nullable=True),
    sa.Column('PRC_ENTREGA_CLI_ID', sa.Integer(), nullable=True),
    sa.Column('PRC_TIME_ID', sa.Integer(), nullable=True),
    sa.Column('PRC_CONHEC_ID', sa.Integer(), nullable=True),
    sa.Column('PRC_ESTR_FISICA_ID', sa.Integer(), nullable=True),
    sa.Column('PRC_ESTR_LOGICA_ID', sa.Integer(), nullable=True),
    sa.Column('PRC_MODELAGEM_ID', sa.Integer(), nullable=True),
    sa.Column('PRC_ROTINA_ID', sa.Integer(), nullable=True),
    sa.Column('PRC_CAPAC_OPERAC_ID', sa.Integer(), nullable=True),
    sa.Column('PRC_FORNE_ITENS_CONS_ID', sa.Integer(), nullable=True),
    sa.Column('PRC_ANALISE_CUSTOS_ID', sa.Integer(), nullable=True),
    sa.Column('PRC_COMPLIANCE_ID', sa.Integer(), nullable=True),
    sa.Column('PRC_AUDITORIA_ID', sa.Integer(), nullable=True),
    sa.Column('PRC_DT_CADASTRO', sa.TIMESTAMP(), nullable=True),
    sa.Column('PRC_DT_ALTERACAO', sa.TIMESTAMP(), nullable=True),
    sa.Column('PRC_DT_EXCLUSAO', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('PRC_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Prc_Cad')
    # ### end Alembic commands ###