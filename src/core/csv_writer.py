# src/core/csv_writer.py

import pandas as pd
import os

class CSVWriter:
    def __init__(self, output_path):
        self.output_path = output_path
        self.writer = pd.ExcelWriter(output_path, engine='xlsxwriter')

    def add_sheet(self, sheet_name, data):
        """Add a sheet to the Excel file with the given data."""
        data.to_excel(self.writer, sheet_name=os.path.splitext(sheet_name)[0], index=False)

    def save(self):
        """Save the Excel file."""
        self.writer.close()
