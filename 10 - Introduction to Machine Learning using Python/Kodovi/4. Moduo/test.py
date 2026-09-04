import joblib
import pandas as pd

# Učitaj model
model = joblib.load("sentiment_model.pkl")

# Pripremi test podatke (moraju imati iste kolone kao pri treniranju)
new_data = pd.DataFrame({
    "review_title": ["Great phone", "Terrible service"],
    "review_text": [
        "I really love this product, battery lasts long and camera is amazing",
        "The product arrived broken and the support was unhelpful"
    ],
    "review_length": [63, 57]  # dužina review_text stringa
})

# Predikcija
predictions = model.predict(new_data)
print(predictions)