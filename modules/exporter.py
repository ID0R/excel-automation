import os
import pandas as pd


def export_to_excel(df: pd.DataFrame, output_path: str):
   
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_excel(output_path, index=False)
