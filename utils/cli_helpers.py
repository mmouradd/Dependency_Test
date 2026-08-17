"""
Rich-based helpers for pretty console output.
"""

from rich.console import Console
from rich.table import Table

console = Console()


def print_summary_table(summary_df):
    table = Table(title="Post Count Per User")
    table.add_column("User ID", justify="right", style="cyan")
    table.add_column("Post Count", justify="right", style="magenta")

    for _, row in summary_df.iterrows():
        table.add_row(str(row["userId"]), str(row["post_count"]))

    console.print(table)
