# plot_A1_meissner.py
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV data
data = pd.read_csv('../data/EXP_A1_Superconductor_Meissner_Log.csv')

# Extract temperature and levitation height
temperature = data['temperature']
levitation_height = data['levitation_height']

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(temperature, levitation_height, color='blue', label='Levitation Height')
plt.plot(temperature, levitation_height, color='blue', linestyle='--', alpha=0.5)

# Set plot properties
plt.xlabel('Temperature (K)')
plt.ylabel('Levitation Height (mm)')
plt.title('Meissner Effect: Levitation Height vs. Temperature')
plt.grid(True)
plt.legend()

# Save and display
plt.savefig('../figures/A1_meissner_plot.png')
plt.show()
