"""Sales Dashboard API - FastAPI + SQLAlchemy.
Totals are calculated in the database (SUM / GROUP BY), not in Python loops,
so reports stay fast on large tables. Seed data comes from sample_data.csv.
Run: pip install -r requirements.txt && uvicorn main:app --reload
"""
from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional
import csv, pathlib
from database import Base, engine, get_db
from models import Sale

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Sales Dashboard API")

def seed(db: Session):
    if db.query(Sale).count() == 0:
        path = pathlib.Path(__file__).parent / "sample_data.csv"
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                db.add(Sale(date=row["date"], region=row["region"],
                            product=row["product"], amount=float(row["amount"])))
        db.commit()

@app.on_event("startup")
def startup():
    seed(next(get_db()))

@app.get("/")
def root():
    return {"message": "Sales Dashboard API is running"}

@app.get("/summary")
def summary(region: Optional[str] = None, product: Optional[str] = None,
            db: Session = Depends(get_db)):
    """Total sales, optionally filtered. Filters are applied in the SQL query,
    so the dashboard only loads the data it needs."""
    q = db.query(Sale)
    if region:
        q = q.filter(Sale.region == region)
    if product:
        q = q.filter(Sale.product == product)
    total = q.with_entities(func.sum(Sale.amount)).scalar() or 0
    by_region = dict(q.with_entities(Sale.region, func.sum(Sale.amount))
                     .group_by(Sale.region).all())
    return {"total_sales": float(total), "orders": q.count(), "by_region": by_region}

@app.get("/sales")
def list_sales(region: Optional[str] = None, product: Optional[str] = None,
               skip: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=100),
               db: Session = Depends(get_db)):
    q = db.query(Sale)
    if region:
        q = q.filter(Sale.region == region)
    if product:
        q = q.filter(Sale.product == product)
    rows = q.offset(skip).limit(limit).all()
    return [{"date": r.date, "region": r.region, "product": r.product, "amount": r.amount}
            for r in rows]

