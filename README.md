# Sensitivity of Cosmic Chronometers to Late-Time Acceleration

**Author:** Mahammad Jamil Dagustany  
**Paper:** Standalone Sensitivity of Cosmic Chronometers to Late-Time Acceleration: A Monte Carlo Null Test  
**Status:** Pre-print (2026)

## 🌌 Overview
This repository contains the Python analysis pipeline used to quantify the statistical resolving power of Cosmic Chronometer (CC) measurements. 

The analysis performs a model selection duel between:
1.  **$\Lambda$CDM Model** (Standard Cosmology)
2.  **Linear Null Model** (Constant Expansion rate, $a \propto t$)

## 📊 Key Features
* **Data Compilation:** Analyzes 31 CC measurements ($0 < z < 2$) from Moresco et al.
* **Model Comparison:** Calculates $\chi^2$, AIC, and BIC for both models.
* **Monte Carlo Simulation:** Generates 1,000 mock datasets to determine the "False Preference Rate" of the null hypothesis under $\Lambda$CDM ground truth.
* **Visualization:** Automatically generates plots comparing the best-fit models against the data.

## 🚀 Usage

### Prerequisites
You need Python 3.x and the following libraries:
* `numpy`
* `scipy`
* `matplotlib`

You can install them via pip:
```bash
pip install numpy scipy matplotlib
Running the Analysis

Clone the repository:

Bash
git clone [https://github.com/XDaGee8/cosmic-chronometers-sensitivity.git](https://github.com/XDaGee8/cosmic-chronometers-sensitivity.git)
Navigate to the folder:

Bash
cd cosmic-chronometers-sensitivity
Run the main script:

Bash
python cc_analysis.py
📉 Results Summary
As detailed in the accompanying manuscript, the analysis yields:

ΔBIC: ≈−1.4 (Indicates no statistical preference for ΛCDM over the Linear Null model).

False Preference Rate: ∼40.2% (The probability that noise mimics a non-accelerating universe).

📜 Citation
If you use this code or methodology, please cite:

Code snippet
@article{Dagustany2026,
  author = {Dagustany, Mahammad Jamil},
  title = {Standalone Sensitivity of Cosmic Chronometers to Late-Time Acceleration: A Monte Carlo Null Test},
  journal = {arXiv e-prints},
  year = {2026},
  month = {Feb}
}
📄 License
MIT License
