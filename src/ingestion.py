# STEP 1 - INGESTION PIPELINE

"""
ingestion.py

Functions for loading and standardizing
market data files.
"""

import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load market data from a CSV file.

    Parameters
    ----------
    filepath : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.
    """
    df = pd.read_csv(filepath)

    return df


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names.

    Example:
    Yield Percent -> yield_percent
    """

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


def convert_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert date column to datetime type.
    """

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    return df


def ingest_market_data(filepath: str) -> pd.DataFrame:
    """
    Complete ingestion workflow.
    """

    df = load_data(filepath)
    df = standardize_columns(df)
    df = convert_dates(df)

    return df