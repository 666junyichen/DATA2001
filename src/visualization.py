"""
Visualization utilities for DATA2001 project.

This module contains functions for creating various plots and visualizations.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_distribution(data, column, bins=30, title=None, figsize=(10, 6)):
    """
    Plot the distribution of a variable.
    
    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame
    column : str
        Column name to plot
    bins : int, default 30
        Number of bins for histogram
    title : str, optional
        Plot title
    figsize : tuple, default (10, 6)
        Figure size (width, height)
    
    Returns
    -------
    matplotlib.figure.Figure
        The created figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.hist(data[column].dropna(), bins=bins, edgecolor='black', alpha=0.7)
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    ax.set_title(title or f'Distribution of {column}')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_scatter(data, x_col, y_col, hue=None, title=None, figsize=(10, 6)):
    """
    Create a scatter plot of two variables.
    
    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame
    x_col : str
        Column name for x-axis
    y_col : str
        Column name for y-axis
    hue : str, optional
        Column name for color coding
    title : str, optional
        Plot title
    figsize : tuple, default (10, 6)
        Figure size (width, height)
    
    Returns
    -------
    matplotlib.figure.Figure
        The created figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    if hue:
        for category in data[hue].unique():
            mask = data[hue] == category
            ax.scatter(data.loc[mask, x_col], data.loc[mask, y_col], 
                      label=category, alpha=0.6)
        ax.legend()
    else:
        ax.scatter(data[x_col], data[y_col], alpha=0.6)
    
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(title or f'{y_col} vs {x_col}')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_correlation_matrix(data, figsize=(10, 8), annot=True):
    """
    Plot a correlation matrix heatmap.
    
    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame
    figsize : tuple, default (10, 8)
        Figure size (width, height)
    annot : bool, default True
        Whether to annotate cells with correlation values
    
    Returns
    -------
    matplotlib.figure.Figure
        The created figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Calculate correlation matrix
    corr = data.select_dtypes(include=[np.number]).corr()
    
    # Create heatmap
    sns.heatmap(corr, annot=annot, cmap='coolwarm', center=0,
                square=True, linewidths=1, ax=ax, vmin=-1, vmax=1,
                fmt='.2f' if annot else None)
    
    ax.set_title('Correlation Matrix')
    
    plt.tight_layout()
    return fig


def plot_boxplot(data, column, by=None, title=None, figsize=(10, 6)):
    """
    Create a box plot for a variable.
    
    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame
    column : str
        Column name to plot
    by : str, optional
        Column name to group by
    title : str, optional
        Plot title
    figsize : tuple, default (10, 6)
        Figure size (width, height)
    
    Returns
    -------
    matplotlib.figure.Figure
        The created figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    if by:
        data.boxplot(column=column, by=by, ax=ax)
        plt.suptitle('')  # Remove default title
    else:
        data.boxplot(column=column, ax=ax)
    
    ax.set_title(title or f'Box Plot of {column}')
    ax.set_ylabel(column)
    
    plt.tight_layout()
    return fig
