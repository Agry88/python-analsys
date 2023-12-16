import dataset
import matplotlib.pyplot as plt

import dataset
def Question1():
    print("探索性分析")

    data = dataset.Dataset()

    # 計算各城市的平均總費用、總收入
    grouped_data = data.groupby('城市').agg({
        '總費用': 'mean',
        '總收入': 'mean'
    })

    # Only Get the first 10 rows
    grouped_data = grouped_data.head(10)

    # 畫出各城市的平均總費用、總收入
    plt.figure(figsize=(10, 5))
    plt.plot(grouped_data['總費用'], label='總費用')
    plt.plot(grouped_data['總收入'], label='總收入')
    plt.legend()
    plt.title('各城市的平均總費用、總收入')
    plt.xlabel('城市')
    plt.ylabel('金額')
    plt.show()



Question1()