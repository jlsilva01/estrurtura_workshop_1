import pandas as pd

from app.pipeline.transform import contact_data_frames

pd_1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
pd_2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})

def testar_concatenacao_da_lista_de_dataframe():
    # arrange = pd.concat([pd_1, pd_2], ignore_index=True),
    # act = contact_data_frames([pd_1, pd_2])
    
    # arrage
    dataframe_list = [pd_1, pd_2]
    dataframe = pd.concat(dataframe_list)
    
    # act
    df = contact_data_frames(dataframe_list)
    
    # assert
    assert df.shape == (4, 2)
    assert dataframe.equals(df)
    assert df.shape != (5, 2)
