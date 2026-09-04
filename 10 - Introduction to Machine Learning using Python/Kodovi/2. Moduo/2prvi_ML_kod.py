import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("D:/Python/libraries/reviews_labeled_cleaned.csv")

X = df['review']
y = df['sentiment']
 
vectorizer = TfidfVectorizer()

X_tfidf = vectorizer.fit_transform(X)
 
model = LogisticRegression()
model.fit(X_tfidf, y)
 
print("\nModel is ready. Enter a review to classify its sentiment.")
print("Type 'exit' to quit.\n")
 
while True:
    user_input = input("Enter a review: ")
    if user_input.lower() == 'exit':
        print("Exiting sentiment classifier.")
        break

    user_tfidf = vectorizer.transform([user_input])
    prediction = model.predict(user_tfidf)[0]

    print(f"Predicted sentiment: {prediction}\n")