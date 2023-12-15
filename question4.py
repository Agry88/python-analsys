import dataset
from sklearn.cluster import KMeans
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd

def Question4():
    # Get data from dataset
    data = dataset.Dataset()

    # Use kmeans to cluster the data by "經度" and "緯度"
    # Assuming 'kmeans' method is available in your Dataset class
    locationData = data[["經度", "緯度 "]]

    # Assuming 'kmeans' method is available in your Dataset class
    clusters = KMeans(n_clusters=3).fit_predict(locationData)

    # Add the cluster column to the data
    data["Cluster"] = clusters

    # Find diference of "年齡", "總收入", "總費用", "總退款" between clusters
    # Assuming 'groupby', 'mean' methods are available in your Dataset class
    result = data.groupby("Cluster").agg({
        "年齡": "mean",
        "總收入": "mean",
        "總費用": "mean",
        "總退款": "mean",
    }).unstack()

    # Display the result
    print("群組差異:")
    print(result)


    selected_cluster = 0
    selected_columns = ['電話服務 ', '多線路服務', '線上安全服務', '線上備份服務', '設備保護計劃', '技術支援計劃', '無限資料下載', "婚姻", "無紙化計費"]
    # Find the cluster with the most people
    selected_cluster_dataframe = data[data["Cluster"] == selected_cluster]
    selected_cluster_dataframe = selected_cluster_dataframe[selected_columns]

    # One-hot encoding
    selected_cluster_dataframe = pd.get_dummies(selected_cluster_dataframe)
    print(selected_cluster_dataframe)

    # 使用Apriori算法找到频繁项集
    frequent_itemsets = apriori(selected_cluster_dataframe, min_support=0.1, use_colnames=True)

    # 使用關聯規則算法生成關聯規則
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

    rules = rules.sort_values(by="confidence", ascending=False)
    print("排序後的關聯規則:")
    print(rules)

    


Question4()
