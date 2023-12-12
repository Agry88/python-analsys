import pandas as pd
import matplotlib.pyplot as plt
import chardet

def Dataset():
    #setting print data
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)

    #setting plt font
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

    # 指定檔案路徑
    file_path = "customer_data.csv"

    # read data
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())

    data = pd.read_csv(file_path, encoding=result['encoding'])

    # 對數值型資料進行中位數填補
    numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
    for column in numeric_columns:
        data[column].fillna(data[column].median(), inplace=True)

    # 對類別型資料進行眾數填補
    category_columns = data.select_dtypes(include='object').columns
    for column in category_columns:
        mode_value = data[column].mode()[0]
        data[column].fillna(mode_value, inplace=True)

    # 顯示資料
    print("資料:")
    print(data)

    return data