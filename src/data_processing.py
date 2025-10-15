"""
Data processing utilities for DATA2001 project.

This module contains functions for loading, cleaning, and preprocessing data.
"""

import pandas as pd
import numpy as np


def load_csv_data(filepath, **kwargs):
    """
    Load data from a CSV file.
    
    Parameters
    ----------
    filepath : str
        Path to the CSV file
    **kwargs : dict
        Additional arguments to pass to pd.read_csv()
    
    Returns
    -------
    pd.DataFrame
        Loaded data
    """
    return pd.read_csv(filepath, **kwargs)


def handle_missing_values(df, strategy='drop', fill_value=None):
    """
    Handle missing values in a DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame
    strategy : str, default 'drop'
        Strategy to handle missing values: 'drop', 'fill', 'mean', 'median'
    fill_value : any, optional
        Value to use when strategy is 'fill'
    
    Returns
    -------
    pd.DataFrame
        DataFrame with missing values handled
    """
    df_clean = df.copy()
    
    if strategy == 'drop':
        df_clean = df_clean.dropna()
    elif strategy == 'fill':
        df_clean = df_clean.fillna(fill_value)
    elif strategy == 'mean':
        df_clean = df_clean.fillna(df_clean.mean())
    elif strategy == 'median':
        df_clean = df_clean.fillna(df_clean.median())
    else:
        raise ValueError(f"Unknown strategy: {strategy}")
    
    return df_clean


def remove_outliers(df, column, method='iqr', threshold=1.5):
    """
    Remove outliers from a DataFrame based on a specific column.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame
    column : str
        Column name to check for outliers
    method : str, default 'iqr'
        Method to detect outliers: 'iqr' or 'zscore'
    threshold : float, default 1.5
        Threshold for outlier detection
        - For IQR: multiplier for IQR (typically 1.5 or 3)
        - For z-score: number of standard deviations (typically 2 or 3)
    
    Returns
    -------
    pd.DataFrame
        DataFrame with outliers removed
    """
    df_clean = df.copy()
    
    if method == 'iqr':
        Q1 = df_clean[column].quantile(0.25)
        Q3 = df_clean[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        df_clean = df_clean[
            (df_clean[column] >= lower_bound) & 
            (df_clean[column] <= upper_bound)
        ]
    elif method == 'zscore':
        z_scores = np.abs((df_clean[column] - df_clean[column].mean()) / 
                         df_clean[column].std())
        df_clean = df_clean[z_scores < threshold]
    else:
        raise ValueError(f"Unknown method: {method}")
    
    return df_clean


def normalize_column(df, column, method='minmax'):
    """
    Normalize a column in a DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame
    column : str
        Column name to normalize
    method : str, default 'minmax'
        Normalization method: 'minmax' or 'zscore'
    
    Returns
    -------
    pd.DataFrame
        DataFrame with normalized column
    """
    df_norm = df.copy()
    
    if method == 'minmax':
        min_val = df_norm[column].min()
        max_val = df_norm[column].max()
        df_norm[column] = (df_norm[column] - min_val) / (max_val - min_val)
    elif method == 'zscore':
        mean_val = df_norm[column].mean()
        std_val = df_norm[column].std()
        df_norm[column] = (df_norm[column] - mean_val) / std_val
    else:
        raise ValueError(f"Unknown method: {method}")
    
    return df_norm
