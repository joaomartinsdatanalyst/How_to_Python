#Como filtrar um dataframe de acordo com um critério de uma coluna específica.
df_filtrado = df[df['nome_da_coluna'] condição]
  ex01: Filtrar por igualdade
    df_filtrado = df[df['cidade'] == 'São Paulo']
  ex02: Filtrar por múltiplas condições (usando & ou |)
    df_filtrado = df[(df['idade'] > 21) & (df['cidade'] == 'São Paulo')]
  ex03: Filtrar por valores em uma lista (usando .isin())
    df_filtrado = df[df['cidade'].isin(['São Paulo', 'Rio de Janeiro'])]
  ex04: Filtrar por valores que NÃO estão em uma lista
    df_filtrado = df[~df['cidade'].isin(['São Paulo', 'Rio de Janeiro'])]
ex05: Filtrar por index
  linhas_filtradas = df[df.index > 1]

#Como filtrar um dataFrame com base em uma coluna de strings que contém datas no formato "dd/mm/yyyy", mantendo a formatação original
hoje = datetime.now()
df_filtrado = df[pd.to_datetime(df['data'], format='%d/%m/%Y') >= hoje]

#Como resetar index do dataframe
df_resetado = df.reset_index()
