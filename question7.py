from dataset import Dataset

# 主題內容：檢查客戶狀態是否與所處的郵遞區號是否相關


#初始化
data = Dataset()

# Group the data by "客戶狀態" and "郵遞區號"
grouped_data = data.groupby(["客戶狀態", "郵遞區號"]).size().reset_index(name='counts')

# Sort the data by "客戶狀態" and "counts"
sorted_data = grouped_data.sort_values(by=["客戶狀態", "counts"], ascending=False)

# Display the result
print("排序後的資料:")
print(sorted_data)