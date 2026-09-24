import pandas as pd
import joblib 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import BayesianRidge
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import LinearSVR
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler


url = "https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv"
df = pd.read_csv(url)

df["Make"] = df["Make"].fillna("")

for col in ["Type", "AirBags", "DriveTrain", "Origin"]:
    df[col] = df[col].fillna(df[col].mode()[0])

for col in ["MPG.city", "EngineSize", "Horsepower", "Weight", "RPM", "Fuel.tank.capacity", "Length", "Width"]:
    df[col] = df[col].fillna(df[col].mean())

df = df.dropna(subset=["Price"])

X = df[["Make", "Type", "AirBags", "DriveTrain", "Origin", "MPG.city", "EngineSize", "Horsepower", "Weight", "RPM", "Fuel.tank.capacity", "Length", "Width"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

preprocessor = ColumnTransformer(
    transformers=[
        ("txt", TfidfVectorizer(), "Make"),
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["Type", "AirBags", "DriveTrain", "Origin"]),
        ("num", MinMaxScaler(), ["MPG.city", "EngineSize", "Horsepower", "Weight", "RPM", "Fuel.tank.capacity", "Length", "Width"])
    ],
    sparse_threshold=0
)

regressors = {
    "Random Forest": RandomForestRegressor(),
    "Naive Bayes": BayesianRidge(),
    "Decision Tree": DecisionTreeRegressor(),
    "LinearSVC": LinearSVR(),
    "Linear Regression": LinearRegression()
}

pipeline_models = {}

for name, regressor in regressors.items():
    pipeline = Pipeline([("preprocessor", preprocessor), ("regressor", regressor)])
    pipeline.fit(X_train, y_train)
    pipeline_models[name] = pipeline

for name, model in pipeline_models.items():
    print(f"Model: {name}\n")
    y_pred = model.predict(X_test)
    print(mean_absolute_error(y_test, y_pred) * 1000, "\n", r2_score(y_test, y_pred), "\n")


rfg_pipeline = Pipeline([("preprocessor", preprocessor), ("regressor", RandomForestRegressor())])
rfg_pipeline.fit(X, y)

joblib.dump(rfg_pipeline, "D:/Python/Exercise/5 - Machine Learning/5.8 - Multiple Regressors & Columns/2model.joblib")