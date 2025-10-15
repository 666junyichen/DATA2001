"""
Utility functions for DATA2001 project.

This module contains general utility functions.
"""

import os
import pandas as pd
from datetime import datetime


def get_project_root():
    """
    Get the project root directory.
    
    Returns
    -------
    str
        Path to project root
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_data_path(filename, data_type='raw'):
    """
    Get the full path to a data file.
    
    Parameters
    ----------
    filename : str
        Name of the data file
    data_type : str, default 'raw'
        Type of data: 'raw' or 'processed'
    
    Returns
    -------
    str
        Full path to the data file
    """
    root = get_project_root()
    return os.path.join(root, 'data', data_type, filename)


def save_dataframe(df, filename, data_type='processed', index=False):
    """
    Save a DataFrame to a CSV file.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to save
    filename : str
        Name of the output file
    data_type : str, default 'processed'
        Type of data: 'raw' or 'processed'
    index : bool, default False
        Whether to save the index
    
    Returns
    -------
    str
        Path where file was saved
    """
    filepath = get_data_path(filename, data_type)
    df.to_csv(filepath, index=index)
    return filepath


def log_message(message, log_file='project.log'):
    """
    Log a message with timestamp.
    
    Parameters
    ----------
    message : str
        Message to log
    log_file : str, default 'project.log'
        Name of the log file
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {message}\n"
    
    root = get_project_root()
    log_path = os.path.join(root, log_file)
    
    with open(log_path, 'a') as f:
        f.write(log_entry)


def print_dataframe_info(df, name='DataFrame'):
    """
    Print comprehensive information about a DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to inspect
    name : str, default 'DataFrame'
        Name to display
    """
    print(f"\n{'='*60}")
    print(f"{name} Information")
    print(f"{'='*60}")
    print(f"\nShape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nMissing Values:\n{df.isnull().sum()}")
    print(f"\nMemory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    print(f"\n{'='*60}\n")
