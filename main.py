"""Starter Sales Dashboard API - FastAPI + Pandas skeleton.
Run: pip install -r requirements.txt && uvicorn main:app --reload
Summaries are computed from sample_data.csv in this starter.
Replace it with a PostgreSQL query + summary tables for production.
"""
from fastapi import FastAPI, Query
from typing import Optional
import pandas as pd

app = FastAPI(title="Sales Dashboard API (Starter)")

@app.get("/")
def root():
    return {"message": "Sales Dashboard API starter is running"}

@app.get("/summary")
def summary(region: Optional[str] = None, product: Optional[str] = None):
    """Return total sales, optionally filtered by region/product.
    Filters keep the dashboard fast by returning only the needed data.
    """
    df = pd.read_csv("sample_data.csv")
    if region:
        df = df[df["region"] == region]
    if product:
        df = df[df["product"] == product]
    return {
        "total_sales": float(df["amount"].sum()),
        "orders": int(len(df)),
        "by_region": df.groupby("region")["amount"].sum().to_dict(),
    }
