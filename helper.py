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
    df = pd.read_csv(csv_path, encoding="latin1",header=0
                 ,names= [  'Row_ID',
                            'Order_ID',
                            'Order_Date',
                            'Ship_Date',
                            'Ship_Mode',
                            'Customer_ID',
                            'Customer_Name',
                            'Segment',
                            'Country',
                            'City',
                            'State',
                            'Postal_Code',
                            'Region',
                            'Product_ID',
                            'Category',
                            'Sub-Category',
                            'Product_Name',
                            'Sales',
                            'Quantity',
                            'DiscountPrcnt',
                            'Profit']
                 ,dtype={
                    'Row_ID': 'int',
                    'Order_ID': 'str',
                    'Ship_Mode':'category',
                    'Customer_ID':'str',
                    'Customer_Name':'str',
                    'Segment':'category',
                    'Country':'category',
                    'City':'category',
                    'State':'category',
                    'Postal_Code':'str',
                    'Region':'category',
                    'Product_ID':'str',
                    'Category':'category',
                    'Sub-Category':'category',
                    'Product_Name':'str',
                    'Sales':'float64',
                    'Quantity':'float64',
                    'DiscountPrcnt':'float64',
                    'Profit':'float64'
                                    },
                    parse_dates=['Order_Date',
                                'Ship_Date']
                 )

    df['RealSales'] = df['Sales']/(1-df['DiscountPrcnt'])
    df['DiscountAbs'] = df['RealSales']  -  df['Sales']
    df['ShipingSpeed'] = (df['Ship_Date']-df['Order_Date']).dt.days
    df['Order_Month']=df['Order_Date'].dt.to_period('M').dt.start_time
    print("Dataframe size:", df.shape)
    return df

def saveDF(df :pd.DataFrame,path):
        df.to_csv(path)
    
