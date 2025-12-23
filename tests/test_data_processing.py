"""
Unit tests for data processing module.
"""

import pytest
import pandas as pd
import numpy as np
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.data_processing import (
    handle_missing_values,
    remove_outliers,
    normalize_column
)


@pytest.fixture
def sample_dataframe():
    """Create a sample DataFrame for testing."""
    return pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [1, 2, 3, 100, 5]  # 100 is an outlier
    })


def test_handle_missing_values_drop(sample_dataframe):
    """Test dropping missing values."""
    result = handle_missing_values(sample_dataframe, strategy='drop')
    assert result.shape[0] == 4
    assert not result.isnull().any().any()


def test_handle_missing_values_fill(sample_dataframe):
    """Test filling missing values with a specific value."""
    result = handle_missing_values(sample_dataframe, strategy='fill', fill_value=0)
    assert result.shape[0] == 5
    assert not result.isnull().any().any()
    assert result.loc[2, 'A'] == 0


def test_handle_missing_values_mean(sample_dataframe):
    """Test filling missing values with mean."""
    result = handle_missing_values(sample_dataframe, strategy='mean')
    assert result.shape[0] == 5
    assert not result.isnull().any().any()
    expected_mean = sample_dataframe['A'].mean()
    assert result.loc[2, 'A'] == expected_mean


def test_remove_outliers_iqr(sample_dataframe):
    """Test removing outliers using IQR method."""
    result = remove_outliers(sample_dataframe, 'C', method='iqr', threshold=1.5)
    # The outlier (100) should be removed
    assert 100 not in result['C'].values
    assert result.shape[0] < sample_dataframe.shape[0]


def test_normalize_column_minmax():
    """Test min-max normalization."""
    df = pd.DataFrame({'A': [0, 25, 50, 75, 100]})
    result = normalize_column(df, 'A', method='minmax')
    assert result['A'].min() == 0.0
    assert result['A'].max() == 1.0
    assert result['A'].iloc[2] == 0.5  # Middle value should be 0.5


def test_normalize_column_zscore():
    """Test z-score normalization."""
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
    result = normalize_column(df, 'A', method='zscore')
    # Z-score normalized data should have mean ≈ 0 and std ≈ 1
    assert abs(result['A'].mean()) < 1e-10
    assert abs(result['A'].std() - 1.0) < 1e-10
