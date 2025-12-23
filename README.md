# DATA2001 - School Project

This repository contains the coursework and project files for DATA2001.

## Project Structure

```
DATA2001/
├── data/                   # Data files
│   ├── raw/               # Original, immutable data
│   └── processed/         # Cleaned and processed data
├── notebooks/             # Jupyter notebooks for analysis
├── src/                   # Source code and reusable functions
├── tests/                 # Unit tests
├── docs/                  # Documentation and reports
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/666junyichen/DATA2001.git
cd DATA2001
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

#### Running Jupyter Notebooks

```bash
jupyter notebook
```

Navigate to the `notebooks/` directory and open the desired notebook.

#### Running Tests

```bash
pytest
```

## Project Workflow

1. **Data Collection**: Place raw data files in `data/raw/`
2. **Data Exploration**: Create notebooks in `notebooks/` for initial exploration
3. **Data Processing**: Write reusable functions in `src/` for data cleaning
4. **Analysis**: Perform statistical analysis in notebooks
5. **Visualization**: Create plots and visualizations
6. **Documentation**: Document findings in `docs/`
7. **Testing**: Write tests in `tests/` for your functions

## Contributing

1. Create a new branch for your work
2. Make your changes
3. Test your code
4. Submit a pull request

## Dependencies

See `requirements.txt` for a full list of dependencies. Main libraries include:
- NumPy: Numerical computing
- Pandas: Data manipulation
- Matplotlib/Seaborn: Data visualization
- SciPy: Scientific computing
- Statsmodels: Statistical modeling
- Jupyter: Interactive notebooks

## License

This project is for educational purposes as part of DATA2001 coursework.

## Contact

For questions or issues, please contact the repository owner.