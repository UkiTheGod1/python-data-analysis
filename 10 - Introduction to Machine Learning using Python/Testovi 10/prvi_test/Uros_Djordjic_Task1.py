import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 1. Importovanje i pregled podataka
df = pd.read_csv("messages.csv")
print(df.head())

# 2. Pregled i brisanje praznih redova
df = df.dropna() 
print(df.isna().sum()) 

# 3. Pregled i prepravka kolone "category"
print(df["category"].value_counts()) 

mapping = {'not spam': 'ham'}
 
df['category'] = df['category'].astype(object).replace(mapping).astype("category")
print(df["category"].value_counts())

# 4. Podela podataka
X = df["message"]
y = df["category"]

# 5. Vektorizacija
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)

# 6. Treniranje modela
model = LogisticRegression(max_iter=1000)
model.fit(X_tfidf, y)
print("\nModel is ready.")

# 7. Interaktivni unos poruka
while True:
    user_input = input("Enter a message: ")
    if user_input.lower().strip() == "exit":
        print("Exiting...")
        break
    
    user_tfidf = vectorizer.transform([user_input])
    prediction = model.predict(user_tfidf)[0]
    print(f"Prediction: {prediction}\n")
