# plot_A2_reflectance.py
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV data
data = pd.read_csv('../data/EXP_A2_DVD_PhaseChange_Log.csv')

# Extract pulse duration and reflectance ratio
pulse_duration = data['pulse_duration']
reflectance_ratio = data['reflectance_ratio']

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(pulse_duration, reflectance_ratio, color='red', label='Reflectance Ratio')
plt.plot(pulse_duration, reflectance_ratio, color='red', linestyle='--', alpha=0.5)

# Set plot properties
plt.xlabel('Pulse Duration (ms)')
plt.ylabel('Reflectance Ratio')
plt.title('DVD-RW Phase-Change: Reflectance Ratio vs. Pulse Duration')
plt.grid(True)
plt.legend()

# Save and display
plt.savefig('../figures/A2_reflectance_plot.png')
plt.show()
