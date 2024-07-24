# src/core/csv_loader.py

import pandas as pd

class CSVLoader:
    def __init__(self, input_dir):
        self.input_dir = input_dir

    def get_columns(self, file_path):
        """Get column names from a CSV file."""
        df = pd.read_csv(file_path, nrows=0)
        return list(df.columns)

    def load_data(self, file_path, columns):
        """Load data from a CSV file with specific columns."""
        return pd.read_csv(file_path, usecols=columns)
