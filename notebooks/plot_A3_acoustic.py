# plot_A3_acoustic.py
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV data
data = pd.read_csv('../data/EXP_A3_Acoustic_Levitation_Sweep.csv')

# Extract frequency and node height
frequency = data['frequency']
node_height = data['node_height']

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(frequency, node_height, color='green', label='Node Height')
plt.plot(frequency, node_height, color='green', linestyle='--', alpha=0.5)

# Set plot properties
plt.xlabel('Frequency (Hz)')
plt.ylabel('Node Height (mm)')
plt.title('Acoustic Levitation: Node Height vs. Frequency')
plt.grid(True)
plt.legend()

# Save and display
plt.savefig('../figures/A3_acoustic_plot.png')
plt.show()
