# Nama  : Nurhayati Ningsih
# NIM   : F1D02410085
# Kelas : C

import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
import random

CSV_FILE = "supermarket_sales.csv"

def load_data():
    if os.path.exists(CSV_FILE):
        try:
            df = pd.read_csv(CSV_FILE)
            df.columns = df.columns.str.replace(r'\s+', '_', regex=True).str.lower().str.strip()
            
            if "sales" in df.columns and "total" not in df.columns:
                df = df.rename(columns={"sales": "total"})

            if "date" in df.columns:
                df["date"] = pd.to_datetime(df["date"], errors="coerce")
            
            for c in ["unit_price", "quantity", "tax_5%", "total", "cogs", "gross_income", "rating"]:
                if c in df.columns:
                    df[c] = pd.to_numeric(df[c], errors="coerce")
            
            df = df.dropna(subset=["total"]).reset_index(drop=True)
            print(f"Data loaded dari {CSV_FILE}, {len(df)} baris")
            return df
        except Exception as e:
            print(f"Gagal baca CSV: {e}")

    print("CSV tidak ditemukan atau gagal, pakai data sample...")
    return _generate_sample()

def _generate_sample():
    random.seed(42)
    np.random.seed(42)
    branches = {"A": "Yangon", "B": "Naypyitaw", "C": "Mandalay"}
    products = ["Health and beauty", "Electronic accessories", "Home and lifestyle", "Sports and travel", "Food and beverages", "Fashion accessories"]
    cust_types = ["Member", "Normal"]
    genders = ["Male", "Female"]
    payments = ["Ewallet", "Cash", "Credit card"]
    rows = []
    base = datetime(2019, 1, 1)

    for i in range(100):
        br = random.choice(list(branches.keys()))
        up = round(random.uniform(10, 100), 2)
        qty = random.randint(1, 10)
        cogs = round(up * qty, 2)
        tax = round(cogs * 0.05, 2)
        rows.append({
            "invoice_id": f"INV-{i+1:03d}", "branch": br, "city": branches[br],
            "customer_type": random.choice(cust_types), "gender": random.choice(genders),
            "product_line": random.choice(products), "unit_price": up, "quantity": qty,
            "tax_5%": tax, "total": round(cogs + tax, 2),
            "date": base + timedelta(days=random.randint(0, 89)),
            "time": f"{random.randint(10,21):02d}:{random.randint(0,59):02d}",
            "payment": random.choice(payments), "cogs": cogs,
            "gross_margin_percentage": 4.7619, "gross_income": tax,
            "rating": round(random.uniform(4.0, 10.0), 1),
        })
    return pd.DataFrame(rows)

def get_filter_options(df):
    options = {}
    for col in ["branch", "city", "customer_type", "gender", "product_line", "payment"]:
        if col in df.columns:
            options[col] = ["Semua"] + sorted(df[col].dropna().unique().tolist())
    return options