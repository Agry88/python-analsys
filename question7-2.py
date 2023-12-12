from dataset import Dataset
import pandas as pd


# 主題內容：檢查客戶狀態是否與所處的郵遞區號類別是否相關

#初始化
data = Dataset()

# Use pandas cut to group the data by "郵遞區號"
data["郵遞區號類別"] = pd.cut(data["郵遞區號"], 5, labels=["第一群", "第二群", "第三群", "第四群", "第五群"])
# Show "郵遞區號類別"'s max 郵遞區號 and min 郵遞區號
print("郵遞區號類別:")
print(data.groupby("郵遞區號類別").agg({
  "郵遞區號": ["max", "min"],
}))

# Show the data
print("資料:")
grouped_data = data.groupby(["客戶狀態"]).agg({
  "郵遞區號類別": "value_counts",
})
print(grouped_data)