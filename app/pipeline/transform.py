from typing import List

import pandas as pd


def contact_data_frames(dataframe_list: List[pd.DataFrame]) -> pd.DataFrame:

    """
    Função para transformar uma lista de dataframes em um único dataframe

    """

    return pd.concat(dataframe_list)