# Sales Data Dashboard API

FastAPI + SQLAlchemy project that returns sales summaries for a dashboard.

## What it does
- Returns total sales and order counts
- Filters by region and product, e.g. `/summary?region=North`
- Groups totals by region, calculated in the database with SUM / GROUP BY

## Run it
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
Docs: http://127.0.0.1:8000/docs

## Tests
```bash
pytest
```

