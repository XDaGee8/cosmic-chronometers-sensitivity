```markdown
# Calibrating the Standalone Detection Threshold of Cosmic Chronometers

**Author:** Mahammad Jamil Dagustany  
**Paper:** Calibrating the Standalone Detection Threshold of Cosmic Chronometers: A Monte Carlo Null-Sensitivity Test  
**Status:** Pre-print (2026)

## 🌌 Overview
This repository contains the Python analysis pipeline used to calibrate the intrinsic curvature-resolving power of Cosmic Chronometer (CC) measurements. 

Instead of testing cosmological models directly, this work treats the CC dataset as a **differential curvature detector**. The analysis performs a sensitivity calibration by comparing the standard model against a null-sensitivity boundary:
1.  **$\Lambda$CDM Model** (Fiducial Ground Truth)
2.  **Null-Sensitivity Boundary** (Constant Expansion, $a \propto t$)

## 📊 Key Features
* **Data Compilation:** Analyzes 31 CC measurements ($0 < z < 2$) from Moresco et al.
* **Detector Response:** Calculates $\chi^2$, AIC, and BIC to determine if acceleration is statistically resolvable.
* **Monte Carlo Calibration:** Generates 1,000 mock datasets to measure the "False Preference Rate" (the frequency with which noise mimics a non-accelerating universe).
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
```

### Running the Analysis

1. Clone the repository:
```bash
git clone https://github.com/XDaGee8/cosmic-chronometers-sensitivity.git
```

2. Navigate to the folder:
```bash
cd cosmic-chronometers-sensitivity
```

3. Run the main script:
```bash
python cc_analysis.py
```

## 📉 Results Summary
As detailed in the accompanying manuscript, the analysis yields:

- **BIC:** (Indicates no statistical preference for $\Lambda$CDM over the Linear Null model).  
- **False Preference Rate:** (The probability that noise mimics a non-accelerating universe).  

## 📜 Citation
If you use this code or methodology, please cite:

```bibtex
@article{Dagustany2026,
  author = {Dagustany, Mahammad Jamil},
  title = {Standalone Sensitivity of Cosmic Chronometers to Late-Time Acceleration: A Monte Carlo Null Test},
  journal = {arXiv e-prints},
  year = {2026},
  month = {Feb}
}
```

## 📄 License
MIT License
```
