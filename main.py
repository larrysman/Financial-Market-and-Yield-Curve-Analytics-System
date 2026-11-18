# TESTING SCRIPT

from src.ingestion import ingest_market_data

from src.validation import (
    generate_validation_report,
    validation_passed
)

from src.database import (
    create_connection,
    save_bond_data,
    load_bond_data,
    close_connection
)

from src.analytics import (
    plot_yield_curve,
    calculate_yield_spread,
    classify_yield_curve
)


df = ingest_market_data(
    "data/clean_bond_yields.csv"
)

report = generate_validation_report(
    df
)

print(report)

if validation_passed(report):

    conn = create_connection()

    save_bond_data(
        df,
        conn
    )

    data = load_bond_data(conn)

    spread = calculate_yield_spread(
        data
    )

    curve_type = classify_yield_curve(
        spread
    )

    plot_yield_curve(data)

    print(
        f"10Y-2Y Spread: {spread:.2f}%"
    )

    print(
        f"Curve Type: {curve_type}"
    )

    close_connection(conn)

else:

    print(
        "Validation failed."
    )