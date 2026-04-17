import os
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBRegressor

DEFAULT_DATA_PATHS = [
    os.getenv("DATA_PATH", "").strip(),
    r"C:\Users\mitra\Downloads\customer_booking_data_for_airline_case_study - customer_booking.xlsx",
    str(Path("data") / "customer_booking.xlsx"),
]
MODEL_PATH = Path("models") / "booking_price_model.joblib"
TARGET_COL = "booking amount"


def resolve_data_path() -> Path:
    for candidate in DEFAULT_DATA_PATHS:
        if candidate and Path(candidate).exists():
            return Path(candidate)
    raise FileNotFoundError(
        "Dataset not found. Set DATA_PATH env var or place file at data/customer_booking.xlsx"
    )


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    if {"purchase_lead", "length_of_stay"}.issubset(out.columns):
        out["lead_stay_ratio"] = out["purchase_lead"] / (out["length_of_stay"] + 1)

    if {"flight_hour", "purchase_lead"}.issubset(out.columns):
        out["hour_lead_interaction"] = out["flight_hour"] * np.log1p(out["purchase_lead"])

    service_columns = [
        col
        for col in ["wants_extra_baggage", "wants_preferred_seat", "wants_in_flight_meals"]
        if col in out.columns
    ]
    if service_columns:
        out["service_request_count"] = out[service_columns].sum(axis=1)

    return out


def build_pipeline(categorical_cols: list[str], numeric_cols: list[str]) -> Pipeline:
    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categorical",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
                    ]
                ),
                categorical_cols,
            ),
            (
                "numeric",
                Pipeline(steps=[("imputer", SimpleImputer(strategy="median"))]),
                numeric_cols,
            ),
        ]
    )

    regressor = XGBRegressor(
        objective="reg:squarederror",
        random_state=42,
        n_jobs=1,
        tree_method="hist",
        n_estimators=700,
        max_depth=5,
        learning_rate=0.01,
        subsample=0.9,
        colsample_bytree=0.8,
        min_child_weight=5,
        reg_alpha=0.0,
        reg_lambda=5.0,
    )

    return Pipeline(steps=[("preprocessor", preprocessor), ("model", regressor)])


def train_and_save() -> None:
    data_path = resolve_data_path()
    print(f"Using dataset: {data_path}")

    df = pd.read_excel(data_path)

    for col in df.columns:
        if df[col].isna().any():
            mode_values = df[col].mode(dropna=True)
            if not mode_values.empty:
                df[col] = df[col].fillna(mode_values.iloc[0])

    df = engineer_features(df)

    if TARGET_COL not in df.columns:
        raise ValueError(f"Target column '{TARGET_COL}' not found in dataset")

    # Keep zero values in features; only filter zero target rows.
    y = df[TARGET_COL].copy()
    X = df.drop(columns=[TARGET_COL]).copy()

    valid_target_mask = y > 0
    X = X.loc[valid_target_mask].copy()
    y = y.loc[valid_target_mask].copy()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    categorical_cols = X_train.select_dtypes(include=["object", "string"]).columns.tolist()
    numeric_cols = X_train.select_dtypes(exclude=["object", "string"]).columns.tolist()

    model = build_pipeline(categorical_cols, numeric_cols)
    model.fit(X_train, y_train)

    pred = model.predict(X_test)
    r2 = r2_score(y_test, pred)
    rmse = mean_squared_error(y_test, pred) ** 0.5
    mae = mean_absolute_error(y_test, pred)

    print(f"R2: {r2:.4f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"MAE: {mae:.2f}")

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    artifact = {
        "model": model,
        "feature_columns": X.columns.tolist(),
        "target_col": TARGET_COL,
        "metrics": {"r2": float(r2), "rmse": float(rmse), "mae": float(mae)},
    }
    joblib.dump(artifact, MODEL_PATH)
    print(f"Saved model artifact: {MODEL_PATH}")


if __name__ == "__main__":
    train_and_save()
