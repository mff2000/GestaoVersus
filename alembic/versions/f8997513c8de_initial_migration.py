"""initial_migration

Revision ID: f8997513c8de
Revises: 
Create Date: 2024-06-23 21:02:34.507926

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f8997513c8de'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('GER_INDIC',
    sa.Column('GER_INDIC_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('GER_INDIC_TIPO', sa.String(length=255), nullable=True),
    sa.Column('GER_INDIC_NOME', sa.String(length=255), nullable=True),
    sa.Column('GER_INDIC_RESPONS', sa.String(length=255), nullable=True),
    sa.Column('GER_INDIC_CALCULO', sa.Decimal(10,2), nullable=True),
    sa.Column('GER_INDIC_OBSERV', sa.Text(), nullable=True),
    sa.Column('GER_INDIC_DT_CRIACAO', sa.DateTime(), nullable=False),
    sa.Column('GER_INDIC_DT_ALTERACAO', sa.DateTime(), nullable=True),
    sa.Column('GER_INDIC_DT_EXCLUSAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('GER_INDIC_ID')
    )
    op.create_table('GER_TIME',
    sa.Column('GER_TIME_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('GER_TIME_NOME', sa.String(length=256), nullable=False),
    sa.Column('GER_TIME_SIGLA', sa.String(length=20), nullable=False),
    sa.Column('GER_TIME_LIDER_ID', sa.Integer(), nullable=True),
    sa.Column('GER_TIME_DT_CRIACAO', sa.DateTime(), nullable=False),
    sa.Column('GER_TIME_DT_ALTERACAO', sa.DateTime(), nullable=True),
    sa.Column('GER_TIME_DT_EXCLUSAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('GER_TIME_ID')
    )
    op.create_table('GER_USUARIOS',
    sa.Column('GER_USU_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('GER_USU_NOME', sa.String(length=256), nullable=False),
    sa.Column('GER_USU_EMAIL', sa.String(length=256), nullable=False),
    sa.Column('GER_USU_SENHA', sa.String(length=256), nullable=True),
    sa.Column('GER_USU_GRUPOPERMISSAO', sa.String(length=256), nullable=True),
    sa.Column('GER_USU_TIME', sa.String(length=256), nullable=True),
    sa.Column('GER_USU_OBSERVACOES', sa.String(length=999), nullable=False),
    sa.Column('GER_USU_DT_CRIACAO', sa.DateTime(), nullable=False),
    sa.Column('GER_USU_DT_ALTERACAO', sa.DateTime(), nullable=True),
    sa.Column('GER_USU_DT_INATIVACAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('GER_USU_ID')
    )
    op.create_table('PRC_ANALISE_CUSTOS',
    sa.Column('PRC_ANALISE_CUSTOS_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('PRC_ID', sa.Integer(), nullable=False),
    sa.Column('PRC_ANALISE_CUSTOS_CUSTO_FIXO', sa.String(length=255), nullable=True),
    sa.Column('PRC_ANALISE_CUSTOS_CUSTO_VARIAVEL', sa.String(length=255), nullable=True),
    sa.Column('PRC_ANALISE_CUSTOS_CUSTO_TOTAL', sa.String(length=255), nullable=True),
    sa.Column('PRC_ANALISE_CUSTOS_GASTOS_GERAIS', sa.String(length=255), nullable=True),
    sa.Column('PRC_ANALISE_CUSTOS_INVESTIMENTO', sa.String(length=255), nullable=True),
    sa.Column('PRC_ANALISE_CUSTOS_LUCRO', sa.String(length=255), nullable=True),
    sa.Column('PRC_ANALISE_CUSTOS_ROIC', sa.String(length=255), nullable=True),
    sa.Column('PRC_ANALISE_CUSTOS_OBSERVACOES', sa.Text(), nullable=True),
    sa.Column('PRC_ANALISE_CUSTOS_DT_CRIACAO', sa.DateTime(), nullable=False),
    sa.Column('PRC_ANALISE_CUSTOS_DT_ALTERACAO', sa.DateTime(), nullable=True),
    sa.Column('PRC_ANALISE_CUSTOS_DT_EXCLUSAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('PRC_ANALISE_CUSTOS_ID')
    )
    op.create_table('PRC_ATIV_CAD',
    sa.Column('PRC_ATIV_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('PRC_ID', sa.Integer(), nullable=False),
    sa.Column('PRC_ATIV_TITULO', sa.String(length=256), nullable=False),
    sa.Column('PRC_ATIV_ANEXOS', sa.String(length=256), nullable=True),
    sa.Column('PRC_ATIV_OBS', sa.String(length=999), nullable=True),
    sa.Column('PRC_ATIV_TIME_ID', sa.Integer(), nullable=True),
    sa.Column('PRC_ATIV_DT_CADASTRO', sa.DateTime(), nullable=False),
    sa.Column('PRC_ATIV_DT_ALTERACAO', sa.DateTime(), nullable=True),
    sa.Column('PRC_ATIV_DT_EXCLUSAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('PRC_ATIV_ID')
    )
    op.create_table('PRC_AUDITORIA',
    sa.Column('PRC_AUDITORIA_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('PRC_AUDITORIA_TIPO', sa.String(length=255), nullable=True),
    sa.Column('PRC_AUDITORIA_PERIODIC', sa.String(length=255), nullable=True),
    sa.Column('PRC_AUDITORIA_DESCRICAO', sa.Text(), nullable=True),
    sa.Column('PRC_AUDITORIA_OBSERV', sa.Text(), nullable=True),
    sa.Column('PRC_AUDITORIA_DT_CRIACAO', sa.DateTime(), nullable=False),
    sa.Column('PRC_AUDITORIA_DT_ALTERACAO', sa.DateTime(), nullable=True),
    sa.Column('PRC_AUDITORIA_DT_EXCLUSAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('PRC_AUDITORIA_ID')
    )
    op.create_table('PRC_CAPAC_OPERAC',
    sa.Column('PRC_CAPAC_OPERAC_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('PRC_CAPAC_OPERAC_ELEMEN', sa.String(length=255), nullable=True),
    sa.Column('PRC_CAPAC_OPERAC_UN_MED', sa.String(length=255), nullable=True),
    sa.Column('PRC_CAPAC_OPERAC_VALOR', sa.String(length=255), nullable=True),
    sa.Column('PRC_CAPAC_OPERAC_DESCR', sa.Text(), nullable=True),
    sa.Column('PRC_CAPAC_OPERAC_OBSERV', sa.Text(), nullable=True),
    sa.Column('PRC_CAPAC_OPERAC_DT_CRIACAO', sa.DateTime(), nullable=False),
    sa.Column('PRC_CAPAC_OPERAC_DT_ALTERACAO', sa.DateTime(), nullable=True),
    sa.Column('PRC_CAPAC_OPERAC_DT_EXCLUSAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('PRC_CAPAC_OPERAC_ID')
    )
    op.create_table('PRC_COMPLIANCE',
    sa.Column('PRC_COMPLIANCE_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('PRC_COMPLIANCE_TIPO_REGRA', sa.String(length=255), nullable=True),
    sa.Column('PRC_COMPLIANCE_DESCR_REGRA', sa.Text(), nullable=True),
    sa.Column('PRC_COMPLIANCE_SITUACAO_REGRA', sa.String(length=255), nullable=True),
    sa.Column('PRC_COMPLIANCE_OBSERV', sa.Text(), nullable=True),
    sa.Column('PRC_COMPLIANCE_DT_CRIACAO', sa.DateTime(), nullable=False),
    sa.Column('PRC_COMPLIANCE_DT_ALTERACAO', sa.DateTime(), nullable=True),
    sa.Column('PRC_COMPLIANCE_DT_EXCLUSAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('PRC_COMPLIANCE_ID')
    )
    op.create_table('PRC_CONHEC',
    sa.Column('PRC_CONHEC_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('PRC_CONHEC_TEC', sa.Text(), nullable=True),
    sa.Column('PRC_CONHEC_GEST', sa.Text(), nullable=True),
    sa.Column('PRC_CONHEC_RELAC', sa.Text(), nullable=True),
    sa.Column('PRC_CONHEC_DESCR', sa.Text(), nullable=True),
    sa.Column('PRC_CONHEC_OBSERV', sa.Text(), nullable=True),
    sa.Column('PRC_CONHEC_DT_CRIACAO', sa.DateTime(), nullable=False),
    sa.Column('PRC_CONHEC_DT_ALTERACAO', sa.DateTime(), nullable=True),
    sa.Column('PRC_CONHEC_DT_EXCLUSAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('PRC_CONHEC_ID')
    )
    op.create_table('PRC_ENTREGA_CLI',
    sa.Column('PRC_ENTREGA_CLI_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('PRC_ID', sa.Integer(), nullable=False),
    sa.Column('PRC_ENTREGA_CLI_DESCR', sa.Text(), nullable=True),
    sa.Column('PRC_ENTREGA_CLI_OBSERV', sa.Text(), nullable=True),
    sa.Column('PRC_ENTREGA_CLI_DT_CRIACAO', sa.DateTime(), nullable=False),
    sa.Column('PRC_ENTREGA_CLI_DT_ALTERACAO', sa.DateTime(), nullable=True),
    sa.Column('PRC_ENTREGA_CLI_DT_EXCLUSAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('PRC_ENTREGA_CLI_ID')
    )
    op.create_table('PRC_ESTR_FISICA',
    sa.Column('PRC_ESTR_FISICA_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('PRC_ESTR_FISICA_DESCR', sa.Text(), nullable=True),
    sa.Column('PRC_ESTR_FISICA_NECESSID', sa.Text(), nullable=True),
    sa.Column('PRC_ESTR_FISICA_OBSERV', sa.Text(), nullable=True),
    sa.Column('PRC_ESTR_FISICA_DT_CRIACAO', sa.DateTime(), nullable=False),
    sa.Column('PRC_ESTR_FISICA_DT_ALTERACAO', sa.DateTime(), nullable=True),
    sa.Column('PRC_ESTR_FISICA_DT_EXCLUSAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('PRC_ESTR_FISICA_ID')
    )
    op.create_table('PRC_ESTR_LOGICA',
    sa.Column('PRC_ESTR_LOGICA_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('PRC_ESTR_LOGICA_DESCR', sa.Text(), nullable=True),
    sa.Column('PRC_ESTR_LOGICA_NECESSID', sa.Text(), nullable=True),
    sa.Column('PRC_ESTR_LOGICA_OBSERV', sa.Text(), nullable=True),
    sa.Column('PRC_ESTR_LOGICA_DT_CRIACAO', sa.DateTime(), nullable=False),
    sa.Column('PRC_ESTR_LOGICA_DT_ALTERACAO', sa.DateTime(), nullable=True),
    sa.Column('PRC_ESTR_LOGICA_DT_EXCLUSAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('PRC_ESTR_LOGICA_ID')
    )
    op.create_table('PRC_FORNE_ITENS_CONS',
    sa.Column('PRC_FORNE_ITENS_CONS_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('PRC_FORNE_ITENS_CONS_NOME', sa.String(length=255), nullable=True),
    sa.Column('PRC_FORNE_ITENS_CONS_UN_MED', sa.String(length=20), nullable=True),
    sa.Column('PRC_FORNE_ITENS_CONS_VALOR', sa.String(length=20), nullable=True),
    sa.Column('PRC_FORNE_ITENS_CONS_OBSERV', sa.Text(), nullable=True),
    sa.Column('PRC_FORNE_ITENS_CONS_DT_CRIACAO', sa.DateTime(), nullable=False),
    sa.Column('PRC_FORNE_ITENS_CONS_DT_ALTERACAO', sa.DateTime(), nullable=True),
    sa.Column('PRC_FORNE_ITENS_CONS_DT_EXCLUSAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('PRC_FORNE_ITENS_CONS_ID')
    )
    op.create_table('PRC_MODELAGEM',
    sa.Column('PRC_MODELAGEM_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('PRC_MODELAGEM_TIPO', sa.String(length=255), nullable=True),
    sa.Column('PRC_MODELAGEM_DESCR', sa.Text(), nullable=True),
    sa.Column('PRC_MODELAGEM_OBSERV', sa.Text(), nullable=True),
    sa.Column('PRC_MODELAGEM_DT_CRIACAO', sa.DateTime(), nullable=False),
    sa.Column('PRC_MODELAGEM_DT_ALTERACAO', sa.DateTime(), nullable=True),
    sa.Column('PRC_MODELAGEM_DT_EXCLUSAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('PRC_MODELAGEM_ID')
    )
    op.create_table('PRC_ROTINA',
    sa.Column('PRC_ROTINA_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('PRC_ROTINA_TIPO', sa.String(length=255), nullable=True),
    sa.Column('PRC_ROTINA_START', sa.String(length=255), nullable=True),
    sa.Column('PRC_ROTINA_DESCR', sa.Text(), nullable=True),
    sa.Column('PRC_ROTINA_OBSERV', sa.Text(), nullable=True),
    sa.Column('PRC_ROTINA_DT_CRIACAO', sa.DateTime(), nullable=False),
    sa.Column('PRC_ROTINA_DT_ALTERACAO', sa.DateTime(), nullable=True),
    sa.Column('PRC_ROTINA_DT_EXCLUSAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('PRC_ROTINA_ID')
    )
    op.create_table('PRJ_GESTAO',
    sa.Column('PRJ_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('PRJ_TIPO', sa.String(length=20), nullable=False),
    sa.Column('PRJ_PAI', sa.Integer(), nullable=True),
    sa.Column('PRJ_NIVEL', sa.Integer(), nullable=False),
    sa.Column('PRJ_CODIGO', sa.String(length=20), nullable=False),
    sa.Column('PRJ_TITULO', sa.String(length=256), nullable=False),
    sa.Column('PRJ_DESCRICAO', sa.String(length=999), nullable=True),
    sa.Column('PRJ_RESPONS_ID', sa.Integer(), nullable=True),
    sa.Column('PRJ_EXECUTORES_ID', sa.Integer(), nullable=True),
    sa.Column('PRJ_PROCESSO_ID', sa.Integer(), nullable=True),
    sa.Column('PRJ_AREA', sa.String(length=256), nullable=True),
    sa.Column('PRJ_OBSERV_HISTOR', sa.String(length=999), nullable=True),
    sa.Column('PRJ_DT_CRIACAO', sa.DateTime(), nullable=False),
    sa.Column('PRJ_DT_PREVISTA', sa.DateTime(), nullable=True),
    sa.Column('PRJ_DT_PRORROGADA', sa.DateTime(), nullable=True),
    sa.Column('PRJ_DT_CONCLUSAO', sa.DateTime(), nullable=True),
    sa.Column('PRJ_DT_EXCLUSAO', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('PRJ_ID')
    )
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
    op.drop_table('PRJ_GESTAO')
    op.drop_table('PRC_ROTINA')
    op.drop_table('PRC_MODELAGEM')
    op.drop_table('PRC_FORNE_ITENS_CONS')
    op.drop_table('PRC_ESTR_LOGICA')
    op.drop_table('PRC_ESTR_FISICA')
    op.drop_table('PRC_ENTREGA_CLI')
    op.drop_table('PRC_CONHEC')
    op.drop_table('PRC_COMPLIANCE')
    op.drop_table('PRC_CAPAC_OPERAC')
    op.drop_table('PRC_AUDITORIA')
    op.drop_table('PRC_ATIV_CAD')
    op.drop_table('PRC_ANALISE_CUSTOS')
    op.drop_table('GER_USUARIOS')
    op.drop_table('GER_TIME')
    op.drop_table('GER_INDIC')
    # ### end Alembic commands ###
