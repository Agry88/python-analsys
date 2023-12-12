import dataset

def Question2():
    print("Question 2: ")
    data = dataset.Dataset()

    # Assuming 'groupby' and 'sum' methods are available in your Dataset class
    grouped_data = data.groupby("城市").sum("總收入")

    print("Grouped Data:")
    print(grouped_data)

Question2()
