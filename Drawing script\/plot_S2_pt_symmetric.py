# plot_S2_pt_symmetric.py
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV data
data = pd.read_csv('../data/EXP_Sim_PT2x2_Params.csv')

# Extract data
gamma = data['gamma']
eigenvalue_real_1 = data['eigenvalue_real_1']
eigenvalue_imag_1 = data['eigenvalue_imag_1']
eigenvalue_real_2 = data['eigenvalue_real_2']
eigenvalue_imag_2 = data['eigenvalue_imag_2']

# Create two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

# Plot the real eigenvalues
ax1.plot(gamma, eigenvalue_real_1, 'o-', color='blue', label='Eigenvalue 1 (Real)')
ax1.plot(gamma, eigenvalue_real_2, 's--', color='red', label='Eigenvalue 2 (Real)')
ax1.set_ylabel('Real Part of Eigenvalues')
ax1.set_title('PT-Symmetric 2x2 Dimer: Eigenvalues ​​vs. Gain/Loss (γ)')
ax1.grid(True)
ax1.legend()

# Plot the imaginary eigenvalues
ax2.plot(gamma, eigenvalue_imag_1, 'o-', color='blue', label='Eigenvalue 1 (Imag)')
ax2.plot(gamma, eigenvalue_imag_2, 's--', color='red', label='Eigenvalue 2 (Imag)')
ax2.set_xlabel('Gain/Loss Parameter (γ)')
ax2.set_ylabel('Imaginary Part of Eigenvalues')
ax2.grid(True)
ax2.legend()

# Adjust the layout
plt.tight_layout()

# Save and display
plt.savefig('../figures/S2_pt_symmetric_plot.png')
plt.show()
