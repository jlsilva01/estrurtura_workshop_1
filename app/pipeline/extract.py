"""Módulo para extrair dados de arquivos excel."""

import glob
import os  # biblioteca para manipular arquivos e pastas
from typing import List  # biblioteca para listar arquivos

import pandas as pd  # biblioteca para manipular dataframes

path = 'data/input'   # caminho da pasta input


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """Ler arquivos de data/input, retornar lista de dataframes.

    Args:
        input_path (str): caminho da pasta input

    Returns:
        lista de dataframes
    """
    all_files = glob.glob(
        os.path.join(path, '*.xlsx')
    )   # lista todos os arquivos .xlsx da pasta

    dataframe_list = []   # lista para armazenar os dataframes
    for file in all_files:
        dataframe_list.append(
            pd.read_excel(file)
        )   # adiciona o dataframe na lista

    return dataframe_list   # retorna a lista de dataframes


# Normalmente isso é feito para testar a função
# Se o arquivo for executado diretamente, o if é verdadeiro
# Se o arquivo for importado/chamar atraves de outro arquivo
# com o main.py, por exekplo, o if é falso

if __name__ == '__main__':
    dataframes = extract_from_excel(path)   # chama a função extract_from_excel
    print(dataframes)   # imprime a lista de dataframes
    print('Hello World!')
