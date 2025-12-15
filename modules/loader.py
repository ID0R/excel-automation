import os
import pandas as pd


def load_file(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    _, ext = os.path.splitext(file_path)

    try:
        if ext.lower() == ".csv":
            return pd.read_csv(file_path, on_bad_lines="skip")

        if ext.lower() in [".xls", ".xlsx"]:
            return pd.read_excel(file_path)

    except Exception as e:
        raise RuntimeError(f"Failed to load file: {e}")

    raise ValueError("Unsupported file format. Use CSV or Excel.")
