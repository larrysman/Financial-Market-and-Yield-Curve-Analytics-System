# STEP 2 - VALIDATION PIPELINE

"""
validation.py

Functions for validating financial market datasets.
"""

import pandas as pd


def check_missing_values(df: pd.DataFrame) -> int:
    """
    Count total missing values.
    """
    return df.isnull().sum().sum()


def check_duplicates(df: pd.DataFrame) -> int:
    """
    Count duplicate rows.
    """
    return df.duplicated().sum()


def check_invalid_maturities(df: pd.DataFrame) -> pd.DataFrame:
    """
    Identify invalid maturities.

    Maturities should be positive.
    """

    return df[df["maturity_years"] <= 0]


def check_invalid_yields(df: pd.DataFrame) -> pd.DataFrame:
    """
    Identify unrealistic yield values.

    For this project:
    Yield < 0 or > 20 is flagged.
    """

    return df[
        (df["yield_percent"] < 0)
        | (df["yield_percent"] > 20)
    ]


def generate_validation_report(df: pd.DataFrame) -> dict:
    """
    Generate a summary validation report.
    """

    report = {
        "missing_values": check_missing_values(df),
        "duplicate_rows": check_duplicates(df),
        "invalid_maturities": len(
            check_invalid_maturities(df)
        ),
        "invalid_yields": len(
            check_invalid_yields(df)
        )
    }

    return report


def validation_passed(report: dict) -> bool:
    """
    Check whether the dataset passed all
    validation checks.

    Parameters
    ----------
    report : dict
        Validation report dictionary.

    Returns
    -------
    bool
        True if all checks pass,
        otherwise False.
    """

    return all(
        value == 0
        for value in report.values()
    )