import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

url = 'https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv'
df = pd.read_table(url, header=None, names=['label', 'message'])

X = df["message"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

classifiers = {
    "Decision Tree": DecisionTreeClassifier(),
    "Naive Bayes": MultinomialNB(),
    "Logistic Regression": LogisticRegression(),
    "Random Forest": RandomForestClassifier(),
    "Linear SVC" : LinearSVC()
}

models = {}

for name, classifier in classifiers.items():
    pipeline = Pipeline([("vectorizer", TfidfVectorizer()), ("classifier", classifier)])
    pipeline.fit(X_train, y_train)
    models[name] = pipeline

for name, model in models.items():
    y_pred = model.predict(X_test)
    print(f"{name}\n", classification_report(y_test, y_pred), "\n", confusion_matrix(y_test, y_pred), "\n")

# LinearSVC se pokazao kao najprecizniji

final_pipeline = Pipeline([("vectorizer", TfidfVectorizer()), ("classifier", LinearSVC())])
final_pipeline.fit(X, y)

joblib.dump(final_pipeline, "D:/Python/Exercise/5 - Machine Learning/5.7 - Pipeline Multi Classifiers/2model.joblib")
