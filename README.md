# BI_painel_covid_c1
Parte da nota da C1 da disciplina de BI onde o objetivo é filtrar a base de dados sobre a COVID-19 no estado do Espirito Santo para pegar as mortes causadas pela doença no município de Cariacica em que a pessoa possuía como comorbidade tabagismo

A pasta chromedreve contém uma classe que auxilia em manter o driver do chrome sempre atualizado para a etapa de download do .csv com os dados

O arquivo baixa_relatorio_microdados.py é a etapa onde é feioto o download do csv direto do portal do covid do estado do ES.

O arquivo dataset.py é onde são manilulados os DataFrames para a obtenção das tabelas fato e da tabela dimensão. Nele há a variavel caminho que deve ser ajustada com o caminho onde o arquivo MICRODADOS.csv é baixado na su amaquina

O arquivo database.py contém os scripts para enviar os datasets ao banco de dados, o banco escolhido é o PostgreSQL e nesse arquivo contém a variavel engine que deve ser configurada conforme os seus dados do banco. com a utilização do metodo to_sql() não é necessário um script de criação de tabelas. 

O arquivo main.py é o arquivo que deve ser executado para rodar o processo por completo.
