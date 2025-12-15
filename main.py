import argparse
from modules.loader import load_file
from modules.cleaner import clean_data


def main():
    parser = argparse.ArgumentParser(description="Excel Automation Tool")
    parser.add_argument("--input", required=True, help="Path to input file")

    args = parser.parse_args()

    df = load_file(args.input)
    print(f"Loaded data: {df.shape[0]} rows, {df.shape[1]} columns")

    df_clean = clean_data(df)
    print(f"After cleaning: {df_clean.shape[0]} rows, {df_clean.shape[1]} columns")


if __name__ == "__main__":
    main()
