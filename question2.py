import dataset

def Question2():
    print("Question 2: ")
    data = dataset.Dataset()

    # Assuming 'groupby', 'sum', 'sort_values' methods are available in your Dataset class
    grouped_data = data.groupby("城市").agg({"總收入": "sum", "總費用": "sum", "總退款": "sum"})
    sorted_data = grouped_data.sort_values(by="總收入", ascending=False)

    # Display only the top third rows with specific columns
    result = sorted_data.head(3)[["總收入", "總費用", "總退款"]]

    print("Top Third Data:")
    print(result)

Question2()
