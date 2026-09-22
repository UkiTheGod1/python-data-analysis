import joblib

# 1. Učitavanje sačuvanog modela
model = joblib.load("D:/Python/Exercise/5 - Machine Learning/5.7 - Pipeline Multi Classifiers/2model.joblib")

# 2. Test primeri (kombinacija tipičnih HAM i SPAM poruka)
test_messages = [
    "Hey, what time are we meeting for coffee today?",
    "URGENT! You have won a $1000 Walmart gift card. Click here to claim NOW!",
    "Can you please send me the report before the end of the day?",
    "FREE ENTRY: Win tickets to the Champions League final! Text WIN to 80085.",
    "Sorry I missed your call, I'll call you back in 5 minutes.",
]

# 3. Predikcija
predictions = model.predict(test_messages)

# 4. Prikaz rezultata
print("--- TESTIRANJE PRODUCJSKOG MODELA ---\n")
for msg, pred in zip(test_messages, predictions):
    print(f"[{pred.upper()}] -> {msg}")