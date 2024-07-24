# main.py

from src.core.csv_loader import CSVLoader
from src.core.csv_writer import CSVWriter
from src.core.user_interface import UserInterface
from config.settings import INPUT_DIR, OUTPUT_FILE
import os

def main():
    # Initialize components
    csv_loader = CSVLoader(INPUT_DIR)
    csv_writer = CSVWriter(OUTPUT_FILE)
    user_interface = UserInterface()

    # Process each CSV file
    for file_name in os.listdir(INPUT_DIR):
        if file_name.endswith('.csv'):
            file_path = os.path.join(INPUT_DIR, file_name)
            columns = csv_loader.get_columns(file_path)
            selected_columns = user_interface.select_columns(file_name, columns)
            data = csv_loader.load_data(file_path, selected_columns)
            csv_writer.add_sheet(file_name, data)

    # Save the output file
    csv_writer.save()

if __name__ == "__main__":
    main()
