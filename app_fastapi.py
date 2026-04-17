from typing import Any

import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI, HTTPException

MODEL_PATH = "models/booking_price_model.joblib"

app = FastAPI(title="Airline Booking Price API", version="1.0.0")


def load_artifact() -> dict[str, Any]:
    try:
        return joblib.load(MODEL_PATH)
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=503,
            detail=(
                "Model artifact not found. Run: python train_api_model.py "
                "after setting DATA_PATH."
            ),
        ) from exc


@app.get("/health")
def health() -> dict[str, Any]:
    artifact = load_artifact()
    return {
        "status": "ok",
        "model_loaded": True,
        "metrics": artifact.get("metrics", {}),
    }


@app.post("/predict")
def predict(payload: dict[str, Any]) -> dict[str, Any]:
    artifact = load_artifact()
    model = artifact["model"]
    feature_columns = artifact["feature_columns"]
    target_col = artifact.get("target_col", "booking amount")

    input_frame = pd.DataFrame([payload])
    input_frame = input_frame.drop(columns=[target_col], errors="ignore")

    # Align incoming payload with training schema.
    input_frame = input_frame.reindex(columns=feature_columns)

    # Add engineered features if missing and source columns are present.
    if "lead_stay_ratio" in feature_columns and {
        "purchase_lead",
        "length_of_stay",
    }.issubset(input_frame.columns):
        if pd.isna(input_frame.loc[0, "lead_stay_ratio"]):
            input_frame.loc[0, "lead_stay_ratio"] = input_frame.loc[0, "purchase_lead"] / (
                input_frame.loc[0, "length_of_stay"] + 1
            )

    if "hour_lead_interaction" in feature_columns and {
        "flight_hour",
        "purchase_lead",
    }.issubset(input_frame.columns):
        if pd.isna(input_frame.loc[0, "hour_lead_interaction"]):
            input_frame.loc[0, "hour_lead_interaction"] = input_frame.loc[0, "flight_hour"] * np.log1p(
                input_frame.loc[0, "purchase_lead"]
            )

    if "service_request_count" in feature_columns:
        cols = [
            c
            for c in [
                "wants_extra_baggage",
                "wants_preferred_seat",
                "wants_in_flight_meals",
            ]
            if c in input_frame.columns
        ]
        if cols and pd.isna(input_frame.loc[0, "service_request_count"]):
            input_frame.loc[0, "service_request_count"] = input_frame[cols].sum(axis=1).iloc[0]

    prediction = float(model.predict(input_frame)[0])

    return {
        "predicted_booking_amount": round(prediction, 2),
        "currency": "USD",
    }
