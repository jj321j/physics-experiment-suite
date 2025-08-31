# plot_S1_ising.py
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV data
data = pd.read_csv('../data/EXP_Sim_Ising_MonteCarlo_Params.csv')

# Extract data
temperature = data['temperature']
magnetization = data['magnetization']
susceptibility = data['susceptibility']
heat_capacity = data['heat_capacity']

# Create multiple subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12), sharex=True)

# Plot magnetization
ax1.plot(temperature, magnetization, 'o-', color='blue', label='Magnetization')
ax1.set_ylabel('Magnetization (M)')
ax1.set_title('2D Ising Model: Observables vs. Temperature')
ax1.grid(True)
ax1.legend()

# Plot magnetic susceptibility
ax2.plot(temperature, susceptibility, 'o-', color='red', label='Susceptibility')
ax2.set_ylabel('Susceptibility (χ)')
ax2.grid(True)
ax2.legend()

# Plot heat capacity
ax3.plot(temperature, heat_capacity, 'o-', color='green', label='Heat Capacity')
ax3.set_xlabel('Temperature (J/k_B)')
ax3.set_ylabel('Heat Capacity (C_v)')
ax3.grid(True)
ax3.legend()

# Adjust the layout
plt.tight_layout()

# Save and display
plt.savefig('../figures/S1_ising_plot.png')
plt.show()
