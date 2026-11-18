# STEP 3 - DATABASE PIPELINE

"""
database.py

Functions for storing and retrieving
financial market data using SQLite.
"""

import sqlite3
import pandas as pd


def create_connection(
    database_name: str = "market_data.db"
) -> sqlite3.Connection:
    """
    Create SQLite database connection.

    Parameters
    ----------
    database_name : str

    Returns
    -------
    sqlite3.Connection
    """

    connection = sqlite3.connect(
        database_name
    )

    return connection


def save_bond_data(
    df: pd.DataFrame,
    connection: sqlite3.Connection,
    table_name: str = "bond_yields"
) -> None:
    """
    Save DataFrame to database.
    """

    df.to_sql(
        table_name,
        connection,
        if_exists="replace",
        index=False
    )

    print(
        f"Data saved to table '{table_name}'."
    )


def load_bond_data(
    connection: sqlite3.Connection,
    table_name: str = "bond_yields"
) -> pd.DataFrame:
    """
    Load table from database.
    """

    query = f"""
    SELECT *
    FROM {table_name}
    """

    df = pd.read_sql(
        query,
        connection
    )

    return df


def close_connection(
    connection: sqlite3.Connection
) -> None:
    """
    Close database connection.
    """

    connection.close()

    print(
        "Database connection closed."
    )