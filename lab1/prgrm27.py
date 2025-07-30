import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load data
path = input("Enter path to person.csv: ")
df = pd.read_csv(path)

# Assume last column is the label “cheats?” with values Yes/No
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Split, train, predict
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model = DecisionTreeClassifier(criterion='entropy')  # approximates C5.0
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
