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

    # Drop the Nan data
    data = data.dropna()

    # 顯示資料
    print("資料:")
    print(data)

    return data