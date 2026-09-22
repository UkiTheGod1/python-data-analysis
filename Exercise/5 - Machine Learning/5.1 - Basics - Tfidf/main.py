import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = {
    'Poruka': [
        "Hej, jesi li za kafu danas?",
        "VAŠA NAGRADA ČEKA! Kliknite na link odmah!",
        "Podsećamo vas na sastanak u 14h.",
        "Besplatne okretaje dobijate odmah, samo se registrujte na naš sajt!",
        "Možeš li mi poslati onaj fajl od juče?",
        "HITNO! Tvoja kartica je blokirana. Pošalji podatke odmah!",
        "Vidimo se sutra na treningu.",
        "Čestitamo! Osvojili ste iPhone 15, javi se!"
    ],
    'Labela': ['ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam']
}

df = pd.DataFrame(data)

X = df["Poruka"]
y = df["Labela"]

vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_tfidf, y)

while True:
    user_input = input("Unesi poruku za proveru:")
    if user_input == "exit":
        break

    user_tfidf = vectorizer.transform([user_input])
    prediction = model.predict(user_tfidf)[0]
    print(prediction)

