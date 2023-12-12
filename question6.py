import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataset import Dataset
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

#初始化
data = Dataset()

# 簡單分群
data["AgeGroup"] = pd.cut(data["年齡"], 3, labels=["青年", "中年", "老年"])


# 用來做關聯規則的Function
def getAssociation(dataframe, selected_cluster_label):
  selected_columns = ['電話服務 ', '多線路服務', '線上安全服務', '線上備份服務', '設備保護計劃', '技術支援計劃', '無限資料下載', "婚姻", "無紙化計費"]
  # Find the cluster with the most people
  selected_cluster_dataframe = dataframe[dataframe["AgeGroup"] == selected_cluster_label]
  selected_cluster_dataframe = selected_cluster_dataframe[selected_columns]

  # One-hot encoding
  selected_cluster_dataframe = pd.get_dummies(selected_cluster_dataframe)

  # 使用Apriori算法找到频繁项集
  frequent_itemsets = apriori(selected_cluster_dataframe, min_support=0.1, use_colnames=True)

  # 使用關聯規則算法生成關聯規則
  rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

  rules = rules.sort_values(by="confidence", ascending=False)
  return rules

# 顯示不同分群的關聯規則
for label in ["青年", "中年", "老年"]:
  print("年齡分群:", label)
  print(getAssociation(data, label))