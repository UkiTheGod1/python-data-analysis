import pandas as pd
from sklearn.model_selection import train_test_split
 
df = pd.read_csv("reviews_labeled_cleaned.csv")

X = df["review"]
y = df["sentiment"]
 
# Split the data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
 
# Display sizes of the resulting sets
print("Training set size:", len(X_train))
print("Test set size:", len(X_test))
 
# Display class distribution in the training and test sets
print("Training set class distribution:")
print(y_train.value_counts())
print("Test set class distribution:")
print(y_test.value_counts())