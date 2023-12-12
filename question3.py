import dataset
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def build_decision_tree():
    # Get data from dataset
    data = dataset.Dataset()

    labelencoder = LabelEncoder()
    data_le = data.apply(labelencoder.fit_transform)
    X = data_le.drop(columns=["客戶狀態"])
    y = data_le["客戶狀態"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build a decision tree model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")

# Call the function to build and evaluate the decision tree
build_decision_tree()
