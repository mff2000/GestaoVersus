from sqlalchemy.orm import sessionmaker
from modelos import Session, tabela_prc_cad

def atualizar_prc_cad(prc_cad_id, prc_tipo, prc_pai, prc_nivel, prc_codigo, prc_nome, prc_gerenciamento, prc_missao, prc_dono_id, prc_exig_qualidade, prc_indic_id, prc_entrega_cli_id, prc_time_id, prc_conhecimento_id, prc_estrutura_fisica_id, prc_estrutura_logica_id, prc_modelagem_id, prc_rotina_id, prc_capacidade_operacional_id, prc_fornecedores_itens_consumo_id, prc_analise_custos_id, prc_compliance_id, prc_auditoria_id):
    """
    Função para atualizar um registro da tabela PRC_CAD.

    Args:
        prc_cad_id (int): ID do registro a ser atualizado.
        ... (mesmos argumentos da função criar_prc_cad do Passo 4 completo)
    """
    with Session() as session:
        registro = session.query(tabela_prc_cad).filter_by(PRC_CAD=prc_cad_id).first()
        if registro:
            registro.PRC_TIPO = prc_tipo
            registro.PRC_PAI = prc_pai
            registro.PRC_NIVEL = prc_nivel
            registro.PRC_CODIGO = prc_codigo
            registro.PRC_NOME = prc_nome
            registro.PRC_GERENCIAMENTO = prc_gerenciamento
            registro.PRC_MISSAO = prc_missao
            registro.PRC_DONO_ID = prc_dono_id
            registro.PRC_EXIG_QUALID = prc_exig_qualidade
            registro.PRC_INDIC_ID = prc_indic_id
            registro.PRC_ENTREGA_CLI_ID = prc_entrega_cli_id
            registro.PRC_TIME_ID = prc_time_id
            registro.PRC_CONHEC_ID = prc_conhecimento_id
            registro.PRC_ESTR_FISICA_ID = prc_estrutura_fisica_id
            registro.PRC_ESTR_LOGICA_ID = prc_estrutura_logica_id
            registro.PRC_MODELAGEM_ID = prc_modelagem_id
            registro.PRC_ROTINA_ID = prc_rotina_id
            registro.PRC_CAPAC_OPERAC_ID = prc_capacidade_operacional_id
            registro.PRC_FORNE_ITENS_CONS_ID = prc_fornecedores_itens_consumo_id
            registro.PRC_ANALISE_CUSTOS_ID = prc_analise_custos_id
            registro.PRC_COMPLIANCE_ID = prc_compliance_id
            registro.PRC_AUDITORIA_ID = prc_auditoria_id
            session.commit()