import joblib

pipeline = joblib.load("product_category_model.pkl")

while True:
    user_input = input("Enter product title (or 'exit'): ")
    if user_input.lower() == "exit":
        break

    prediction = pipeline.predict([user_input])[0] 
    print(f"Predicted category: {prediction}")