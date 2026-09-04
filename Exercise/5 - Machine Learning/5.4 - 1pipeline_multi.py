import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder

url = "https://raw.githubusercontent.com/campusx-official/laptop-price-predictor-regression-project/main/laptop_data.csv"
df_ceo = pd.read_csv(url)

df = df_ceo.filter(items=["Company", "Inches", "Ram", "Price", "Memory", "Gpu", "Cpu", "ScreenResolution"])

df["Price"] = df["Price"] / 90
df["Ram"] = df["Ram"].str.replace("GB", "")
df["Ram"] = pd.to_numeric(df["Ram"], errors="coerce")

df[["Storage_Raw", "Bonus_Storage_Raw"]] = df["Memory"].str.split("+", expand=True)

df[["Storage", "Storage_Type"]] = df["Storage_Raw"].str.split("TB |GB ", expand=True)
df[["Bonus_Storage", "Bonus_Storage_Type"]] = df["Bonus_Storage_Raw"].str.split("TB |GB ", expand=True)
df["Storage_Type"] = df["Storage_Type"].str.strip()
df["Bonus_Storage"] = df["Bonus_Storage"].fillna(0)

df["Storage"] = pd.to_numeric(df["Storage"], errors="coerce")
df["Storage"] = df["Storage"].astype(int)

df["Bonus_Storage"] = pd.to_numeric(df["Bonus_Storage"], errors="coerce")
df["Bonus_Storage"] = df["Bonus_Storage"].astype(int)

df["Storage"] = df["Storage"].apply(lambda x: x * 1024 if x < 3 else x)
df["Bonus_Storage"] = df["Bonus_Storage"].apply(lambda x: x * 1024 if x < 3 else x)

df.drop(axis=1, columns=["Memory", "Storage_Raw", "Bonus_Storage_Raw"], inplace=True)

X = df[["Company", "Inches", "Ram", "Cpu", "Gpu", "Storage", "Storage_Type", "Bonus_Storage", "Bonus_Storage_Type", "ScreenResolution"]]
y = df["Price"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown='ignore'), ["Company", "Cpu", "Gpu", "Storage_Type", "Bonus_Storage_Type", "ScreenResolution"]),
        ("num", MinMaxScaler(), ["Inches", "Ram", "Storage", "Bonus_Storage"])
    ])

pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("classifier", RandomForestRegressor())
])

pipeline.fit(X, y)

joblib.dump(pipeline, "5.4 - 2model.pkl")


