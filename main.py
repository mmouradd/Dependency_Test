"""
Entry point for the sample project.
Ties together the fetcher, processor, db, and cli_helpers modules.
"""

from src.fetcher import fetch_data
from src.processor import process_data
from src.db import save_summary
from utils.logger import logger
from utils.cli_helpers import print_summary_table


def main():
    logger.info("Starting pipeline...")
    raw = fetch_data()
    processed = process_data(raw)

    print(f"\nTotal records: {len(processed['data'])}")

    if processed["summary"] is not None:
        print_summary_table(processed["summary"])
        save_summary(processed["summary"])
        logger.info("Summary saved to database.")

    logger.info("Done.")


if __name__ == "__main__":
    main()
