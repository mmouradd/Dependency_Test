"""
Processes raw data into a summarized pandas DataFrame.
"""

import pandas as pd


def process_data(raw_data):
    """Convert raw list of dicts into a DataFrame with a title-length column."""
    df = pd.DataFrame(raw_data)
    if "title" in df.columns:
        df["title_length"] = df["title"].str.len()
    if "userId" in df.columns:
        summary = df.groupby("userId").size().reset_index(name="post_count")
        return {"data": df, "summary": summary}
    return {"data": df, "summary": None}
