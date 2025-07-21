import pandas as pd

def load_sales_data(filepath):
    """Load sales data from an Excel file."""
    try:
        df = pd.read_excel(filepath)
        df['Date'] = pd.to_datetime(df['Date']).dt.date
        return df
    except Exception as e:
        raise Exception(f"Error loading file {filepath}: {str(e)}")
