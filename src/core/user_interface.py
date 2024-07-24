# src/core/user_interface.py

from src.utils.validator import validate_column_selection


class UserInterface:
    def select_columns(self, file_name, columns):
        """Display columns and get user selection."""
        print(f"Select columns to extract from {file_name}:")
        for idx, col in enumerate(columns):
            print(f"{idx + 1}. {col}")

        while True:
            try:
                selected_indices = input("Enter column numbers separated by commas: ")
                selected_indices = [int(i.strip()) - 1 for i in selected_indices.split(",")]
                validate_column_selection(columns, selected_indices)
                break  # Exit loop if validation is successful
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

        return [columns[i] for i in selected_indices]
