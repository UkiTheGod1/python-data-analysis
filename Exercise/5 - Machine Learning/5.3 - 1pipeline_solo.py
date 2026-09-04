import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

url = 'https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv'
df = pd.read_table(url, header=None, names=['label', 'message'])

X = df[["message"]]
y = df["label"]

preprocessor = ColumnTransformer(transformers=[("message", TfidfVectorizer(), "message")])

pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("classifier", RandomForestClassifier())
    ])

pipeline.fit(X, y)

joblib.dump(pipeline, "5.3 - 2model.pkl")