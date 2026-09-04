import pandas as pd
import joblib

model = joblib.load("D:/Python/Uro/vezbe/5 - Machine Learning/5.4 - 2model.pkl")

data= pd.DataFrame({
    'Company': ['Apple', 'Dell', 'HP', 'Lenovo', 'Asus', 'Apple'],
    'Inches': [14.2, 13.4, 15.6, 16.0, 14.0, 13.6],
    'ScreenResolution': ['IPS Panel Retina Display 2560x1600', 'Full HD 1920x1080', 'Full HD 1920x1080', 'IPS Panel Full HD 1920x1080', 'Full HD 1920x1080', 'IPS Panel Retina Display 2560x1600'],
    'Cpu': ['Intel Core i7', 'Intel Core i5', 'Intel Core i7', 'Intel Core i9', 'Intel Core i5', 'M2'],
    'Ram': [16, 8, 16, 32, 8, 8],
    'Gpu': ['AMD', 'Intel', 'Nvidia', 'Nvidia', 'Intel', 'Apple'],
    'Storage': [512, 256, 1024, 512, 256, 256],
    'Storage_Type': ['SSD', 'SSD', 'HDD', 'SSD', 'SSD', 'SSD'],
    'Bonus_Storage': [0, 0, 0, 1024, 0, 0],
    'Bonus_Storage_Type': ['None', 'None', 'None', 'HDD', 'None', 'None'],
})

predictions = model.predict(data)
# print(predictions)

print(data)