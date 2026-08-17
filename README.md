# Sample Python Project

A small multi-folder Python project for testing tooling (dependency upgrades, linters, CI, etc.).
10 pinned dependencies spanning HTTP, web, data, db, validation, logging, CLI, and testing.

## Structure

```
sample-python-project/
├── requirements.txt
├── .env.example
├── main.py                 # CLI entrypoint, runs the full pipeline
├── src/
│   ├── __init__.py
│   ├── config.py            # env config (python-dotenv)
│   ├── fetcher.py            # HTTP fetch (requests)
│   ├── processor.py          # data transform (pandas)
│   └── db.py                  # ORM models + persistence (sqlalchemy)
├── api/
│   ├── __init__.py
│   └── app.py                 # HTTP API exposing the pipeline (flask)
├── utils/
│   ├── __init__.py
│   ├── logger.py               # logging setup (loguru)
│   ├── schemas.py              # data validation models (pydantic)
│   └── cli_helpers.py          # pretty console tables (rich)
├── scripts/
│   └── seed_db.py              # standalone CLI script (click)
└── tests/
    ├── __init__.py
    └── test_processor.py       # unit tests (pytest)
```

## Dependencies (`requirements.txt`)
requests, flask, pandas, python-dotenv, click, sqlalchemy, pydantic, loguru, rich, pytest

## Usage

```bash
pip install -r requirements.txt
cp .env.example .env

# Run the full pipeline
python main.py

# Run the Flask API
python -m api.app        # then visit http://localhost:5000/report

# Run the standalone seed script
python scripts/seed_db.py --limit 5

# Run tests
pytest
```
