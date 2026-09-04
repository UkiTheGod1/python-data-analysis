from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    "I love this product",
    "This product is not good",
    "Absolutely fantastic experience",
    "Terrible, I hate it",
    "Not great, not terrible",
    "Okay product, nothing special"
]

bow_vectorizer = CountVectorizer()
X_bow = bow_vectorizer.fit_transform(corpus)

print("Vocabulary:", bow_vectorizer.get_feature_names_out())
print("\nBoW Matrix (Document-Term Matrix):\n", X_bow.toarray())

tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(corpus)
print("\nTF–IDF Matrix:\n", X_tfidf.toarray())