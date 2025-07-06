# Trading Utils

This repository provides tools for analyzing covered call strategies. Core modules expose calculation utilities while `interactive_dashboard.ipynb` offers an interactive notebook.

## Setup

```bash
pip install -r requirements.txt  # installs numpy, pandas, matplotlib, ipywidgets, scipy, flake8, black, pytest
```

## Usage

1. Open `interactive_dashboard.ipynb` in JupyterLab.
2. Adjust the widgets to explore returns, payoff diagrams, Greeks, Monte-Carlo simulations and more.
3. Run the notebook cells to update results.

Unit tests can be run with:

```bash
pytest
```

Code is formatted with Black and checked with flake8.
