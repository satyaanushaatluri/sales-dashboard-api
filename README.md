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

## Infrastructure

Starter Terraform + Kubernetes files. Committing them creates or deploys nothing.

- `terraform/main.tf` — AWS provider + ECR repository only (no EKS cluster, no production deployment).
  ```bash
  cd terraform
  terraform init
  terraform plan
  terraform apply   # only this step creates AWS resources; needs AWS credentials
  ```
- `k8s/deployment.yaml`, `k8s/service.yaml` — 2-replica Deployment (port 8000) and ClusterIP Service.
  ```bash
  kubectl apply -f k8s/
  ```
  See `k8s/README.md` for the image placeholder and database secret you must replace first.

Validate Kubernetes YAML syntax locally:
```bash
python3 -c "import yaml, glob; [yaml.safe_load(open(f)) for f in glob.glob('k8s/*.yaml')]"
```
Terraform formatting was NOT checked in the environment where this was added
because Terraform is not installed there — run `terraform fmt -check` and
`terraform validate` yourself before applying.
