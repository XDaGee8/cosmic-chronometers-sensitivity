import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# --- 1. DATA: The 31 Cosmic Chronometers (z, H, error) ---
# Source: Moresco et al. compilation
data = np.array([
    [0.07, 69.0, 19.6], [0.09, 69.0, 12.0], [0.12, 68.6, 26.2], [0.17, 83.0, 8.0],
    [0.179, 75.0, 4.0], [0.199, 75.0, 5.0], [0.20, 72.9, 29.6], [0.27, 77.0, 14.0],
    [0.28, 88.8, 36.6], [0.352, 83.0, 14.0], [0.3802, 83.0, 13.5], [0.40, 95.0, 17.0],
    [0.4004, 77.0, 10.2], [0.4247, 87.1, 11.2], [0.4497, 92.8, 12.9], [0.47, 89.0, 50.0],
    [0.4783, 80.9, 9.0], [0.48, 97.0, 62.0], [0.593, 104.0, 13.0], [0.68, 92.0, 8.0],
    [0.781, 105.0, 12.0], [0.875, 125.0, 17.0], [0.88, 90.0, 40.0], [0.9, 117.0, 23.0],
    [1.037, 154.0, 20.0], [1.3, 168.0, 17.0], [1.363, 160.0, 33.6], [1.43, 177.0, 18.0],
    [1.53, 140.0, 14.0], [1.75, 202.0, 40.0], [1.965, 186.5, 50.4]
])

z_cc = data[:, 0]
H_cc = data[:, 1]
err_cc = data[:, 2]

# --- 2. MODELS ---

def hubble_lcdm(z, H0, Om):
    """Standard LambdaCDM Model"""
    return H0 * np.sqrt(Om * (1 + z)**3 + (1 - Om))

def hubble_linear(z, H0):
    """Linear Expansion Model (Null Hypothesis): a(t) ~ t"""
    return H0 * (1 + z)

# --- 3. FITTING FUNCTIONS ---

def chi2_lcdm(params):
    H0, Om = params
    model = hubble_lcdm(z_cc, H0, Om)
    return np.sum(((H_cc - model) / err_cc)**2)

def chi2_linear(params):
    H0 = params
    model = hubble_linear(z_cc, H0)
    return np.sum(((H_cc - model) / err_cc)**2)

# Fit LambdaCDM
res_lcdm = minimize(chi2_lcdm, [70, 0.3], bounds=((50, 100), (0, 1)))
chi2_lcdm_val = res_lcdm.fun
k_lcdm = 2

# Fit Linear
res_linear = minimize(chi2_linear, [70], bounds=((50, 100),))
chi2_linear_val = res_linear.fun
k_linear = 1

# --- 4. STATISTICS (BIC/AIC) ---
N = len(z_cc)
bic_lcdm = chi2_lcdm_val + k_lcdm * np.log(N)
bic_linear = chi2_linear_val + k_linear * np.log(N)
delta_bic = bic_linear - bic_lcdm

print(f"Results for Paper Table I:")
print(f"LambdaCDM Chi2: {chi2_lcdm_val:.2f}")
print(f"Linear Chi2: {chi2_linear_val:.2f}")
print(f"Delta BIC: {delta_bic:.2f} (Should be approx -1.4)")

# --- 5. MONTE CARLO SIMULATION ---
np.random.seed(42) # Reproducibility
n_sims = 1000
false_preference_count = 0

# Ground Truth: Best Fit LCDM
H0_true, Om_true = res_lcdm.x
H_true = hubble_lcdm(z_cc, H0_true, Om_true)

for _ in range(n_sims):
    # Generate mock data by adding noise to the TRUE LCDM model
    H_mock = H_true + np.random.normal(0, err_cc)
    
    # Fit both models to the mock data
    def chi2_mock_lcdm(p): return np.sum(((H_mock - hubble_lcdm(z_cc, p[0], p[1]))/err_cc)**2)
    def chi2_mock_lin(p): return np.sum(((H_mock - hubble_linear(z_cc, p[0]))/err_cc)**2)
    
    fit_l = minimize(chi2_mock_lcdm, [70, 0.3], bounds=((50, 100), (0, 1)))
    fit_lin = minimize(chi2_mock_lin, [70], bounds=((50, 100),))
    
    bic_l_sim = fit_l.fun + 2 * np.log(N)
    bic_lin_sim = fit_lin.fun + 1 * np.log(N)
    
    # If Linear has lower BIC, it's a "False Preference" (since we know Truth is LCDM)
    if bic_lin_sim < bic_l_sim:
        false_preference_count += 1

print(f"False Preference Rate: {false_preference_count/n_sims*100:.1f}%")

# --- 6. PLOTTING ---
plt.figure(figsize=(10, 6))
plt.errorbar(z_cc, H_cc, yerr=err_cc, fmt='o', color='black', label='CC Data', alpha=0.6)

z_plot = np.linspace(0, 2, 100)
plt.plot(z_plot, hubble_lcdm(z_plot, res_lcdm.x[0], res_lcdm.x[1]), 'r-', lw=2, label='$\Lambda$CDM (Best Fit)')
plt.plot(z_plot, hubble_linear(z_plot, res_linear.x[0]), 'b--', lw=2, label='Linear Null ($a \propto t$)')

plt.xlabel('Redshift $z$', fontsize=12)
plt.ylabel('$H(z)$ [km/s/Mpc]', fontsize=12)
plt.legend(fontsize=12)
plt.title(f'CC Sensitivity Test: $\Delta$BIC = {delta_bic:.2f}', fontsize=14)
plt.grid(True, alpha=0.3)

# Save the plot
plt.savefig('cc_analysis_plot.png')
print("Plot saved as cc_analysis_plot.png")
plt.show()