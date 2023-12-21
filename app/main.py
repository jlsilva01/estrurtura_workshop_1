from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import contact_data_frames

if __name__ == "__main__":
    dataframe_list = extract_from_excel("data/input")
    print(type(dataframe_list))
    
    dataframe = contact_data_frames(dataframe_list)
    print(type(dataframe))
    
    load_excel(dataframe, "data/output", "output")
    
    print("Done!")
    