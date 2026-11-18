# STEPS 4 - ANALYTICS PIPELINE

"""
analytics.py

Functions for financial market analytics
and yield curve analysis.
"""

import pandas as pd
import matplotlib.pyplot as plt


def plot_yield_curve(
    df: pd.DataFrame,
    output_path: str = "outputs/yield_curve.png"
) -> None:
    """
    Plot and save the yield curve.
    """

    plt.figure(figsize=(8, 5))

    plt.plot(
        df["maturity_years"],
        df["yield_percent"],
        marker="o",
        linewidth=2
    )

    plt.title(
        "Government Bond Yield Curve"
    )

    plt.xlabel(
        "Maturity (Years)"
    )

    plt.ylabel(
        "Yield (%)"
    )

    plt.grid(True)

    plt.savefig(
        output_path,
        bbox_inches="tight"
    )

    plt.close()

    print(
        f"Yield curve saved to {output_path}"
    )


def calculate_yield_spread(
    df: pd.DataFrame
) -> float:
    """
    Calculate 10Y - 2Y spread.
    """

    yield_10y = df.loc[
        df["maturity_years"] == 10,
        "yield_percent"
    ].iloc[0]

    yield_2y = df.loc[
        df["maturity_years"] == 2,
        "yield_percent"
    ].iloc[0]

    spread = (
        yield_10y -
        yield_2y
    )

    return spread


def classify_yield_curve(
    spread: float
) -> str:
    """
    Classify curve shape.
    """

    if spread > 0:
        return "Normal"

    elif spread < 0:
        return "Inverted"

    return "Flat"


def vendor_comparison(
    vendor_a: pd.DataFrame,
    vendor_b: pd.DataFrame
) -> pd.DataFrame:
    """
    Compare yields from two vendors.
    """

    comparison = pd.DataFrame({
        "maturity_years":
            vendor_a["maturity_years"],
        "vendor_a":
            vendor_a["yield_percent"],
        "vendor_b":
            vendor_b["yield_percent"]
    })

    comparison["difference"] = (
        comparison["vendor_a"] -
        comparison["vendor_b"]
    ).abs()

    return comparison
