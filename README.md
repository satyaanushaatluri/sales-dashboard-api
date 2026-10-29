# Sales Data Dashboard API (Starter)

A starter FastAPI + Pandas project that returns sales summaries for a dashboard.

## What it does
- Returns total sales and order counts
- Filters by region and product, e.g. `/summary?region=North`
- Groups totals by region

## Run it
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
Then open http://127.0.0.1:8000/docs

## Next steps
Replace the CSV with PostgreSQL, move calculations to the database, and add summary tables for fast reports.
