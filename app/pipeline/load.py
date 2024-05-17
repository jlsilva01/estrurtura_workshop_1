"""Módulo para carregar os dados em um arquivo excel."""

import os

import pandas as pd


def load_excel(
    dataframe: pd.DataFrame, output_path: str, file_name: str
) -> str:
    """load_excel: Função para receber um dataframe e salvar como excel.

    Args:
        dataframe (pd.DataFrame): dataframe a ser salvo como excel
        output_path (str): caminho para salvar o arquivo excel
        file_name (str): nome do arquivo excel

    Returns:    
        Arquivo Salvo com Sucesso

    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    dataframe.to_excel(f'{output_path}/{file_name}.xlsx', index=False)
    return 'Arquivo Salvo com Sucesso'
