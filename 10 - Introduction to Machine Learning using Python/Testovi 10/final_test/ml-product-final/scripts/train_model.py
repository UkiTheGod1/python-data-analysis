import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

df = pd.read_csv("products.csv")

df = df.dropna()
df = df.drop(columns=['product ID', 'Merchant ID', '_Product Code', 'Number_of_Views', 'Merchant Rating', ' Listing Date  '])
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

mapping = {
    "Fridges": "Fridge Freezers",
    "fridge": "Fridge Freezers",
    "Freezers": "Fridge Freezers",
    "Mobile Phone": "Mobile Phones",
    "CPU": "CPUs"
}

df["category_label"] = df["category_label"].astype(object).replace(mapping).astype("category")

X = df["product_title"]
y = df["category_label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2), min_df=2)),
    ("nb", MultinomialNB())
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

joblib.dump(pipeline, "product_category_model.pkl")
print("Model successfully created!")