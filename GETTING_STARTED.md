# Getting Started with Your DATA2001 Project

Welcome to your DATA2001 school project repository! This guide will help you get up and running quickly.

## What's Been Set Up

Your repository now has a complete professional structure for data science projects:

### 📁 Directory Structure

```
DATA2001/
├── 📊 data/                # Your datasets go here
│   ├── raw/               # Original data files
│   └── processed/         # Cleaned data
├── 📓 notebooks/          # Jupyter notebooks for analysis
├── 🐍 src/                # Reusable Python code
├── ✅ tests/              # Unit tests
├── 📄 docs/               # Documentation and reports
└── ⚙️  Configuration files
```

### 🚀 Quick Start

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/666junyichen/DATA2001.git
   cd DATA2001
   ```

2. **Set up Python environment**:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate it
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Start Jupyter**:
   ```bash
   jupyter notebook
   ```

4. **Open the getting started notebook**:
   - Navigate to `notebooks/00_getting_started.ipynb`
   - This notebook has examples and guidance

### 📚 What's Included

#### Ready-to-Use Python Modules

In the `src/` directory, you'll find:

- **data_processing.py**: Functions for loading, cleaning, and preprocessing data
  - Load CSV files
  - Handle missing values
  - Remove outliers
  - Normalize data

- **visualization.py**: Functions for creating plots
  - Distribution plots
  - Scatter plots
  - Correlation matrices
  - Box plots

- **analysis.py**: Statistical analysis functions
  - Summary statistics
  - T-tests
  - Chi-square tests
  - ANOVA
  - Confidence intervals

- **utils.py**: Helper utilities
  - File path management
  - Data saving
  - Logging
  - DataFrame inspection

#### Example Notebook

The `notebooks/00_getting_started.ipynb` demonstrates:
- How to import libraries
- Loading and exploring data
- Creating basic visualizations
- Where to go next

#### Test Suite

The `tests/` directory contains unit tests. Run them with:
```bash
pytest
```

All 6 tests are currently passing! ✅

### 📝 Next Steps

1. **Add your data**: Place your dataset files in `data/raw/`
2. **Create analysis notebooks**: Use the numbering convention (01_, 02_, etc.)
3. **Write reusable code**: Put functions in the `src/` modules
4. **Document your work**: Add reports to the `docs/` folder
5. **Test your code**: Write tests in the `tests/` directory

### 💡 Tips

- **Large data files**: These are automatically excluded from git (see `.gitignore`)
- **Version control**: Commit your code and notebooks regularly
- **Code organization**: Keep notebooks focused; put reusable code in `src/`
- **Testing**: Write tests for your data processing functions
- **Documentation**: Comment your code and write clear markdown in notebooks

### 🆘 Common Commands

```bash
# Run tests
pytest

# Run tests with verbose output
pytest -v

# Start Jupyter
jupyter notebook

# Install new package and update requirements
pip install package-name
pip freeze > requirements.txt

# Check git status
git status

# Commit changes
git add .
git commit -m "Your message"
git push
```

### 📖 Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Jupyter Notebook Tips](https://jupyter-notebook.readthedocs.io/)

### 🎯 Project Workflow Suggestion

1. **Week 1**: Data collection and exploration
2. **Week 2**: Data cleaning and preprocessing
3. **Week 3**: Statistical analysis
4. **Week 4**: Visualization and reporting
5. **Week 5**: Final report and presentation

Good luck with your DATA2001 project! 🎓
