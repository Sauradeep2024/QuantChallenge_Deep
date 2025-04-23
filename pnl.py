from datetime import datetime, timezone
import sqlite3
import pandas as pd

def compute_pnl(strategy, sql_database):

    with sqlite3.connect(sql_database) as conn:
        df = pd.read_sql_query("SELECT * FROM epex_12_20_12_13", conn)


    # Filter trades by strategy
    df = df[df['strategy'] == strategy]

    if df.empty:
        print(f"No trades found for {strategy}")
        return 0.0
    
    df['income'] = df.apply(
        lambda row: row['quantity'] * row['price'] if row['side'] == 'sell'
        else -row['quantity'] * row['price'], axis=1
    )

    # Compute total PnL
    total_pnl = float(df['income'].sum())

    return {
        "strategy":     strategy,
        "value":        total_pnl,
        "unit":         "euro",
        "capture_time": datetime.now(timezone.utc).isoformat() + "Z"
    }

