# IN501 Unit 9 Assignment

## Getting Started

### Prerequisites
- Python 3.11 (TensorFlow does not support Python 3.14 yet)

### Setup (Windows)
```powershell
# From the repo root
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

### Setup (macOS)
```bash
# From the repo root
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Run the baseline script (Windows)
```powershell
py .\IN501_Mai_Robinson_Samos_Turner_Vega_Unit9_Assignment_Baseline.py
```

### Run the baseline script (macOS)
```bash
python IN501_Mai_Robinson_Samos_Turner_Vega_Unit9_Assignment_Baseline.py
```

## Notes
- The script downloads the MNIST dataset on first run.
- Output images may be saved in the project folder depending on your environment.
- Training time varies by hardware; on CPU expect a few minutes for 5 epochs.
- When plots appear, you may get a save dialog; save or cancel to continue, and close plot windows to let the script proceed.
- There are three `plt.show()` calls, so expect up to three plot windows/prompts.
