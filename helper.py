import kagglehub
import os
import pandas as pd 
def loadData():
    # Downloading dataset
    dataset_name = "vivek468/superstore-dataset-final"
    path = kagglehub.dataset_download(dataset_name)
    print(f"Dataset downloaded in: {path}\n")

    # check folder's contain
    print("Dataset's files:")
    for root, dirs, files in os.walk(path):
        for file in files:
            print(" -", os.path.join(root, file))
    print()

    # Took first csv file
    csv_files = [os.path.join(root, f)
                for root, dirs, files in os.walk(path)
                for f in files if f.lower().endswith(".csv")]

    if not csv_files:
        raise FileNotFoundError("CSV file wasn't found")

    csv_path = csv_files[0]

    # load files to pandas dataframe
    return pd.read_csv(csv_path, encoding="latin1")  
