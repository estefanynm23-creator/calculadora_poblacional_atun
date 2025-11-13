import pandas as pd

def read_csv(file_path):
    """
    Reads a CSV file and returns a pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: DataFrame containing the data from the CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None

def write_csv(data, file_path):
    """
    Writes a pandas DataFrame to a CSV file.
    
    Parameters:
    data (pd.DataFrame): The DataFrame to write to the CSV file.
    file_path (str): The path where the CSV file will be saved.
    """
    try:
        data.to_csv(file_path, index=False)
        print(f"Data successfully written to {file_path}")
    except Exception as e:
        print(f"Error writing to the CSV file: {e}")