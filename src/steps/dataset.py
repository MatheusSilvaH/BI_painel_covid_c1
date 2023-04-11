import pandas as pd
import numpy as np


caminho = r'C:\Users\mathe\Downloads\MICRODADOS.csv'


def gera_df_filtrado():


    # Gera o DataFrame com base no .csv
    df = pd.DataFrame(pd.read_csv(caminho, sep=";", encoding="ISO-8859-1", low_memory=False))

    # Remove todas as linhas em que o municipio seja diferente de CARIACICA
    df.drop(df[df.Municipio != 'CARIACICA'].index, inplace=True)

    # Substitui os valores NaN por uma string vazia
    df.fillna(value='', inplace=True)

    # Remove as linhas que nao possuem data de obito
    df.drop(df[df.DataObito == ''].index, inplace=True)

    # Remove as linhas em que nao possui tabagismo como comorbidade
    df.drop(df[df.ComorbidadeTabagismo != 'Sim'].index, inplace=True)

    # Remove as linh em que o óbito não foi causado pelo COVID-19
    df.drop(df[df.Evolucao != 'Óbito pelo COVID-19'].index, inplace=True)

    # reseta o index do dataframe
    df.reset_index(drop=True, inplace=True)

    df.to_excel(r'.\teste.xlsx')
    return df


def dim_comorbidades():
    comorbidades = ['ComorbidadeRenal', 'ComorbidadeCardio', 'ComorbidadePulmao',
                    'ComorbidadeDiabetes', 'ComorbidadeTabagismo', 'ComorbidadeObesidade']

    return pd.DataFrame({'id': range(1, len(comorbidades)+1),
                                'comorbidade': comorbidades})


def dim_data():
    datas = pd.date_range(start='2020-01-01', end='2040-12-31').tolist()
    return pd.DataFrame({'data': datas,
                         'dia': [d.day for d in datas],
                         'mes': [d.month for d in datas],
                         'ano': [d.year for d in datas]})



def dim_faixa_etaria():
    faixas_etarias = []
    id = []
    for i in range(1, 101, 2):
        inicio = str(i).zfill(2)
        fim = str(i + 1).zfill(2)
        faixa = f'{inicio} a {fim} anos'
        faixas_etarias.append(faixa)
        id.append(i)

    return pd.DataFrame({'id': id, 'faixa_etaria': faixas_etarias})


def dim_bairros():
    bairros_distintos = gera_df_filtrado()['Bairro'].unique()

    return pd.DataFrame({'Bairro': bairros_distintos})
