import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataset import Dataset

#第五題
# 根據 平均長途話費 來進行分群，因為我覺得平均長途話費越高，代表這個人越常打電話，所以我們可以將他分為大量打電話的人和少量打電話的人
# 這樣我們就可以針對不同的人群來設計不同的行銷活動

#初始化
data = Dataset()

# 簡單分群
data["Group"] = pd.cut(data["平均長途話費"], 3, labels=["少量", "中量", "大量"])

# 顯示資料
print("資料:")
grouped_data = data.groupby("Group").agg({
  "年齡": "mean",
  "總收入": "mean",
  "總費用": "mean",
})
print(grouped_data)