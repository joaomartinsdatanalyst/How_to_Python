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

#Como deletar o ultimo item de um lista
del minha_lista[-1]  # Remove o último item

#Como remover acentos
def tratar_nome(text):
    dict_accents = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'ä': 'a', 'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A', 'Ä': 'A',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i', 'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
        'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o', 'ö': 'o', 'Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ô': 'O', 'Ö': 'O',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u', 'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U',
        'ç': 'c', 'Ç': 'C',
        'ñ': 'n', 'Ñ': 'N',
        'ý': 'y', 'ÿ': 'y', 'Ý': 'Y', 'Ÿ': 'Y'
    }

    # Substituir os caracteres acentuados por suas versões sem acento
    for char, replacement in dict_accents.items():
        text = text.replace(char, replacement)
    
    # Remover espaços extras e converter para maiúsculas
    return text.strip().upper()
