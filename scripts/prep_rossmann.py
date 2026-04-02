"""
prep_rossmann.py
----------------
Prepares the Rossmann Store Sales dataset for BSAD 8310 homework assignments.

Input files (download from Kaggle: rossmann-store-sales):
  data/raw/train.csv   -- daily store-level sales
  data/raw/store.csv   -- store metadata

Output files:
  data/processed/rossmann_weekly.csv  -- weekly aggregated (HW1, HW3-HW8)
  data/processed/rossmann_daily.csv   -- daily, Store 1 only (HW2 GAMs/Prophet)

Stores used: 1-30 (mix of types, all with near-complete data)
Period:      2013-01-01 to 2015-07-31

Run once before starting any homework:
  python scripts/prep_rossmann.py
"""

import os
import pandas as pd
import numpy as np

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
STORES = list(range(1, 31))   # stores 1-30

# ── helpers ──────────────────────────────────────────────────────────────────

def check_raw_files():
    missing = [f for f in ["train.csv", "store.csv"]
               if not os.path.exists(os.path.join(RAW_DIR, f))]
    if missing:
        raise FileNotFoundError(
            f"Missing raw data files: {missing}\n"
            "Download from https://www.kaggle.com/c/rossmann-store-sales/data\n"
            f"and place in {RAW_DIR}/"
        )

def load_raw():
    train = pd.read_csv(
        os.path.join(RAW_DIR, "train.csv"),
        parse_dates=["Date"],
        dtype={"StateHoliday": str}
    )
    store = pd.read_csv(os.path.join(RAW_DIR, "store.csv"))
    return train, store

def clean_train(train, store):
    df = train.copy()
    # keep only open days with positive sales and target stores
    df = df[(df["Open"] == 1) & (df["Sales"] > 0) & (df["Store"].isin(STORES))]
    # encode StateHoliday as binary flag
    df["StateHoliday"] = (df["StateHoliday"] != "0").astype(int)
    # merge store metadata
    df = df.merge(store[["Store", "StoreType", "Assortment",
                          "CompetitionDistance", "Promo2"]],
                  on="Store", how="left")
    # fill missing CompetitionDistance with median
    df["CompetitionDistance"] = df["CompetitionDistance"].fillna(
        df["CompetitionDistance"].median()
    )
    return df

def make_weekly(df):
    df = df.copy()
    df["WeekStart"] = df["Date"] - pd.to_timedelta(df["Date"].dt.dayofweek, unit="d")
    agg = (
        df.groupby(["Store", "WeekStart"])
        .agg(
            Sales=("Sales", "sum"),
            Customers=("Customers", "mean"),
            Promo=("Promo", "max"),
            DaysOpen=("Open", "count"),
            StateHoliday=("StateHoliday", "max"),
            SchoolHoliday=("SchoolHoliday", "max"),
            StoreType=("StoreType", "first"),
            Assortment=("Assortment", "first"),
            CompetitionDistance=("CompetitionDistance", "first"),
            Promo2=("Promo2", "first"),
        )
        .reset_index()
    )
    # encode categoricals as integers for convenience
    agg["StoreType"] = agg["StoreType"].map({"a": 1, "b": 2, "c": 3, "d": 4})
    agg["Assortment"] = agg["Assortment"].map({"a": 1, "b": 2, "c": 3})
    agg = agg.sort_values(["Store", "WeekStart"]).reset_index(drop=True)
    return agg

def make_lag_features(weekly):
    df = weekly.copy()
    for store_id, grp in df.groupby("Store"):
        for lag in [1, 4, 13, 26, 52]:
            df.loc[grp.index, f"Sales_lag{lag}"] = grp["Sales"].shift(lag).values
    return df

def make_daily_store1(df):
    return (
        df[df["Store"] == 1]
        .sort_values("Date")
        .reset_index(drop=True)
    )

# ── main ──────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    check_raw_files()

    print("Loading raw data...")
    train, store = load_raw()

    print("Cleaning and merging store metadata...")
    df = clean_train(train, store)

    print("Aggregating to weekly...")
    weekly = make_weekly(df)

    print("Adding lag features...")
    weekly = make_lag_features(weekly)

    out_weekly = os.path.join(PROCESSED_DIR, "rossmann_weekly.csv")
    weekly.to_csv(out_weekly, index=False)
    print(f"Saved {len(weekly):,} rows to {out_weekly}")
    print(f"  Stores: {weekly['Store'].nunique()} | "
          f"Weeks per store (median): {weekly.groupby('Store').size().median():.0f}")

    print("Creating daily Store-1 dataset...")
    daily1 = make_daily_store1(df)
    out_daily = os.path.join(PROCESSED_DIR, "rossmann_daily.csv")
    daily1.to_csv(out_daily, index=False)
    print(f"Saved {len(daily1):,} rows to {out_daily}")

    print("\nDone. Column summary (weekly):")
    print(weekly.dtypes.to_string())

if __name__ == "__main__":
    main()
