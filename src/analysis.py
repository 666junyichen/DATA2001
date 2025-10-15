"""
Statistical analysis utilities for DATA2001 project.

This module contains functions for performing statistical analyses.
"""

import numpy as np
import pandas as pd
from scipy import stats


def calculate_summary_stats(data, column):
    """
    Calculate summary statistics for a column.
    
    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame
    column : str
        Column name
    
    Returns
    -------
    dict
        Dictionary containing summary statistics
    """
    series = data[column].dropna()
    
    return {
        'count': len(series),
        'mean': series.mean(),
        'median': series.median(),
        'std': series.std(),
        'min': series.min(),
        'max': series.max(),
        'q25': series.quantile(0.25),
        'q75': series.quantile(0.75),
        'iqr': series.quantile(0.75) - series.quantile(0.25)
    }


def perform_t_test(sample1, sample2, alternative='two-sided'):
    """
    Perform independent samples t-test.
    
    Parameters
    ----------
    sample1 : array-like
        First sample
    sample2 : array-like
        Second sample
    alternative : str, default 'two-sided'
        Alternative hypothesis: 'two-sided', 'less', or 'greater'
    
    Returns
    -------
    dict
        Dictionary containing test results
    """
    # Remove NaN values
    sample1 = pd.Series(sample1).dropna()
    sample2 = pd.Series(sample2).dropna()
    
    # Perform t-test
    statistic, pvalue = stats.ttest_ind(sample1, sample2, alternative=alternative)
    
    return {
        'statistic': statistic,
        'pvalue': pvalue,
        'sample1_mean': sample1.mean(),
        'sample2_mean': sample2.mean(),
        'sample1_std': sample1.std(),
        'sample2_std': sample2.std(),
        'significant': pvalue < 0.05
    }


def calculate_correlation(data, method='pearson'):
    """
    Calculate correlation matrix.
    
    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame
    method : str, default 'pearson'
        Correlation method: 'pearson', 'spearman', or 'kendall'
    
    Returns
    -------
    pd.DataFrame
        Correlation matrix
    """
    numeric_data = data.select_dtypes(include=[np.number])
    return numeric_data.corr(method=method)


def perform_chi_square_test(data, col1, col2):
    """
    Perform chi-square test of independence.
    
    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame
    col1 : str
        First categorical column
    col2 : str
        Second categorical column
    
    Returns
    -------
    dict
        Dictionary containing test results
    """
    # Create contingency table
    contingency_table = pd.crosstab(data[col1], data[col2])
    
    # Perform chi-square test
    chi2, pvalue, dof, expected = stats.chi2_contingency(contingency_table)
    
    return {
        'chi2_statistic': chi2,
        'pvalue': pvalue,
        'degrees_of_freedom': dof,
        'contingency_table': contingency_table,
        'significant': pvalue < 0.05
    }


def calculate_confidence_interval(data, column, confidence=0.95):
    """
    Calculate confidence interval for the mean.
    
    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame
    column : str
        Column name
    confidence : float, default 0.95
        Confidence level
    
    Returns
    -------
    dict
        Dictionary containing confidence interval information
    """
    series = data[column].dropna()
    n = len(series)
    mean = series.mean()
    std_err = stats.sem(series)
    
    # Calculate confidence interval
    interval = stats.t.interval(confidence, n-1, loc=mean, scale=std_err)
    
    return {
        'mean': mean,
        'confidence_level': confidence,
        'lower_bound': interval[0],
        'upper_bound': interval[1],
        'margin_of_error': interval[1] - mean
    }


def perform_anova(data, value_col, group_col):
    """
    Perform one-way ANOVA test.
    
    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame
    value_col : str
        Column name for values
    group_col : str
        Column name for groups
    
    Returns
    -------
    dict
        Dictionary containing test results
    """
    # Create groups
    groups = [group[value_col].dropna() for name, group in data.groupby(group_col)]
    
    # Perform ANOVA
    statistic, pvalue = stats.f_oneway(*groups)
    
    return {
        'f_statistic': statistic,
        'pvalue': pvalue,
        'num_groups': len(groups),
        'significant': pvalue < 0.05
    }
