from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from src.steps.dataset import gera_df_filtrado, dim_comorbidades, dim_data, dim_faixa_etaria, dim_bairros

# Padrão para a string de conexão "postgresql://[usuario_do_banco]:[senha_do_usuario]@[host]:[porta]/[nome_da_base]"
engine = create_engine('postgresql://postgres:--SUASENHAAQUI--@localhost:5432/covid_data_bi')


def insere_fato_mortes():
    gera_df_filtrado().to_sql('fato_mortes', engine, index=False, if_exists='replace')


def insere_dimensoes():
    dim_comorbidades().to_sql('dim_comorbidades', engine, index=False, if_exists='replace')
    dim_data().to_sql('dim_data', engine, index=False, if_exists='replace')
    dim_faixa_etaria().to_sql('dim_faixa_etaria', engine, index=False, if_exists='replace')
    dim_bairros().to_sql('dim_bairros', engine, index=False, if_exists='replace')

