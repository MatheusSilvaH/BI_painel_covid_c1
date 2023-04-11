from logging import info

from src.steps.baixa_relatorio_microdados import baixa_dataset
from src.steps.database import insere_fato_mortes, insere_dimensoes
from src.steps.dataset import gera_df_filtrado


def main():
    try:
        baixa_dataset()
    except Exception as erro_dataset:
        info(f'Erro ao fazer o download do arquivo CSV. Erro: {erro_dataset}')

    try:
        pass
        gera_df_filtrado()
    except Exception as erro_df:
        info(f'Erro ao filtrar o DataFrame. Erro: {erro_df}')

    try:
        insere_fato_mortes()
        insere_dimensoes()
    except Exception as erro_dw:
        info(f'Erro ao inserir dados da tabela fato no banco. Erro: {erro_dw}')


if __name__ == '__main__':
    main()