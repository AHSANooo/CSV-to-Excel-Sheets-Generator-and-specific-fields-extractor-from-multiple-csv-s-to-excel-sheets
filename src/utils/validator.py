# src/utils/validator.py

def validate_column_selection(columns, selected_indices):
    """Validate that the selected indices are within the range of available columns."""
    if any(idx >= len(columns) or idx < 0 for idx in selected_indices):
        raise ValueError("Invalid column index selected.")
