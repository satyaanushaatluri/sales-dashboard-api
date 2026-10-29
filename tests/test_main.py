from fastapi.testclient import TestClient
from database import Base, engine
import main

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
main.seed(next(main.get_db()))
client = TestClient(main.app)

def test_summary_total():
    r = client.get("/summary")
    assert r.status_code == 200
    assert r.json()["total_sales"] == 4450.0  # 1200 + 850 + 900 + 1500

def test_summary_region_filter():
    r = client.get("/summary", params={"region": "North"})
    assert r.json()["total_sales"] == 2100.0  # 1200 + 900

def test_sales_list():
    assert len(client.get("/sales").json()) == 4

