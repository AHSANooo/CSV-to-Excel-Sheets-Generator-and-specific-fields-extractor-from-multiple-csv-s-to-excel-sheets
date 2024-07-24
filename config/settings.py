# config/settings.py

import os

# Define base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Input directory containing the CSV files
INPUT_DIR = os.path.join(BASE_DIR, '..', 'data', 'input')

# Output directory for the merged output file
OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'data', 'output')

# Output file name
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'merged_output.xlsx')
