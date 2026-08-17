"""
CLI script to fetch data and seed the local database.
Run with: python scripts/seed_db.py --limit 5
"""

import click

from src.fetcher import fetch_data
from src.processor import process_data
from src.db import save_summary
from utils.logger import logger


@click.command()
@click.option("--limit", default=10, help="Number of raw records to process.")
def seed(limit):
    """Fetch data, process it, and store the summary in the database."""
    logger.info(f"Fetching up to {limit} records...")
    raw = fetch_data()[:limit]
    processed = process_data(raw)

    if processed["summary"] is not None:
        save_summary(processed["summary"])
        logger.info("Summary saved to database.")
    else:
        logger.warning("No summary to save.")


if __name__ == "__main__":
    seed()
