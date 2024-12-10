import pandas as pd
import os


def load(path: str):
    """
    Load a dataset from a file (CSV, TXT, Excel, etc.),\
        print its dimensions, and return the dataset.

    Parameters:
        path (str): The path to the file.

    Returns:
        pd.DataFrame: The loaded dataset or None if there's\
            an error.
    """
    try:
        # Get the file extension
        _, ext = os.path.splitext(path)
        ext = ext.lower()

        # Determine the appropriate pandas function based on the file extension
        if ext in ['.csv']:
            dataset = pd.read_csv(path)
        elif ext in ['.xls', '.xlsx']:
            dataset = pd.read_excel(path)
        elif ext in ['.txt']:
            dataset = pd.read_csv(path, delimiter='\t')
        else:
            raise ValueError(f"Unsupported file type: {ext}")

        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset

    except Exception as e:
        print(f"Error: {e}")
        return None
