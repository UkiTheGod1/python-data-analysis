import pandas as pd
import joblib

model = joblib.load("D:/Python/Uro/vezbe/5 - Machine Learning/5.5 - 2model.pkl")

new_messages = pd.DataFrame({
    "text": ["Hey, are you coming to the office tomorrow? I need that report by 10 AM.",
    "URGENT! Your account security has been compromised. Log in at secure-web-verify.com to reset your password immediately!",
    "Winner! You have been selected for a free $500 Amazon gift card. Reply STOP to opt out.",
    "Can you believe that game last night? Total madness in the final minute!"]
})

prediction = model.predict(new_messages)
print(prediction)