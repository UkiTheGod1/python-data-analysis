import joblib
import pandas as pd

loaded_pipeline = joblib.load("D:/Python/Exercise/5 - Machine Learning/5.8 - Multiple Regressors & Columns/2model.joblib")

new_car = pd.DataFrame(
    [
        {
            "Make": "Audi A4",
            "Type": "Midsize",
            "AirBags": "Driver & Passenger",
            "DriveTrain": "Front",
            "Origin": "non-USA",
            "MPG.city": 20,
            "EngineSize": 2.8,
            "Horsepower": 172,
            "Weight": 3395,
            "RPM": 5500,
            "Fuel.tank.capacity": 16.9,
            "Length": 179,
            "Width": 68,
        }
    ]
)

predicted_price = loaded_pipeline.predict(new_car)[0]
print(f"Procenjena cena automobila: ${predicted_price * 1000:,.2f}")