Physics Experiment and Simulation Suite
This repository contains protocols and code for conducting hardware-lite physical experiments and GPU-friendly simulations as part of an A-Level physics curriculum or advanced hobbyist projects. The experiments demonstrate fundamental concepts in condensed matter physics, acoustics, and quantum mechanics, while the simulations explore phase transitions and non-Hermitian systems.
The experiments and simulations are designed to run on a standard laptop (e.g., ThinkPad P73) with minimal hardware add-ons. Data is logged in provided CSV templates, and plotting scripts are available for analysis.

Table of Contents
1.  Overview
2.  Experiments and Simulations
	•  A1: Superconductor Meissner Effect
	•  A2: Phase-Change Material (DVD-RW) Reflectivity
	•  A3: Acoustic Standing Wave / Levitation
	•  S1: 2D Ising Model Monte Carlo Simulation
	•  S2: PT-Symmetric 2x2 Non-Hermitian Dimer Simulation
3.  Requirements
4.  Installation
5.  Usage
6.  Data Logging
7.  Plotting and Analysis
8.  Contributing
9.  License
10.  Procurement Checklist

Overview
This project provides protocols for three physical experiments and two computational simulations:
•  Physical Experiments:
	•  A1: Observe the Meissner effect in a superconductor using a YBCO puck and liquid nitrogen.
	•  A2: Measure reflectivity changes in a rewritable DVD’s phase-change material.
	•  A3: Explore acoustic standing waves and optional levitation using ultrasonic transducers.
•  Simulations:
	•  S1: Study phase transitions in a 2D Ising model using Monte Carlo methods.
	•  S2: Investigate PT-symmetric non-Hermitian systems via eigenvalue analysis of a 2x2 dimer.
All experiments are designed to be accessible with minimal hardware, and simulations are optimized for laptop execution. CSV templates are provided for data logging, and Jupyter notebooks can be generated for visualization.

Experiments and Simulations
A1: Superconductor Meissner Effect
Concept: Demonstrates the Meissner effect in a YBCO superconductor cooled with liquid nitrogen, where a small magnet levitates due to magnetic field expulsion.
Setup:
•  Hardware: YBCO puck, liquid nitrogen, small magnet, cryogenic PPE.
•  Measurement: Record levitation height via photos/videos and measure distances.
•  Safety: Use cryogenic PPE and ensure proper ventilation.
Data Logging: Use EXP_A1_Superconductor_Meissner_Log.csv to record magnet levitation distances and conditions.
Applications:
•  Educational demonstration of superconductivity.
•  Study of magnetic field interactions in Type-II superconductors.
A2: Phase-Change Material (DVD-RW) Reflectivity
Concept: Rewritable DVDs use a GST (Ge-Sb-Te) phase-change layer that toggles between crystalline and amorphous states, altering reflectivity.
Setup:
•  Hardware: Rewritable DVD, DVD burner, webcam/phone camera, image analysis tool (e.g., ImageJ or Python with OpenCV).
•  Steps:
	1.  Burn small test patterns (e.g., 1x1 cm blocks) on the DVD at varying power/pulse settings.
	2.  Capture before/after photos under consistent lighting and angle.
	3.  Analyze grayscale values to compute reflectance ratio.
	4.  Plot reflectance vs. pulse duration to identify the phase transition threshold.
Data Logging: Use EXP_A2_DVD_PhaseChange_Log.csv to log power, pulse duration, and grayscale values.
Applications:
•  Understanding phase-change materials used in optical storage.
•  Exploring material science concepts like amorphous-crystalline transitions.
A3: Acoustic Standing Wave / Levitation
Concept: Standing waves created by ultrasonic transducers form pressure nodes, enabling particle levitation or room-scale wave mapping.
Setup:
•  Minimal Path: Use laptop audio and a small speaker to generate 50–300 Hz waves. Measure sound pressure levels (SPL) with a phone app to map standing waves.
•  Levitation Path: Use a 40 kHz transducer array and driver to create levitation nodes. Sweep frequency and measure node height/stability.
Data Logging: Use EXP_A3_Acoustic_Levitation_Sweep.csv to record frequency, node height, and stability.
Applications:
•  Acoustic wave physics for educational purposes.
•  Ultrasonic levitation for microfluidics, material science, or contactless manipulation.
•  Room acoustics analysis for sound engineering.
S1: 2D Ising Model Monte Carlo Simulation
Concept: Simulates a 2D Ising model to study magnetic phase transitions using Monte Carlo methods.
Setup:
•  Code: Python script (provided in /simulations/S1_Ising_Model).
•  Parameters: Set lattice size and temperature range in EXP_Sim_Ising_MonteCarlo_Params.csv.
•  Observables: Magnetization (M), susceptibility (χ), and heat capacity (C_v) vs. temperature.
•  Expected Result: Critical behavior near T_c ≈ 2.269 (in J/k_B = 1 units).
Applications:
•  Statistical mechanics education.
•  Modeling phase transitions in magnetic systems.
S2: PT-Symmetric 2x2 Non-Hermitian Dimer Simulation
Concept: Simulates a PT-symmetric 2x2 non-Hermitian system to study eigenvalue behavior under gain/loss conditions.
Setup:
•  Code: Python script (provided in /simulations/S2_PT_Symmetric).
•  Parameters: Sweep gain/loss parameter (γ) in EXP_Sim_PT2x2_Params.csv.
•  Observables: Plot real and imaginary eigenvalues to identify the exceptional point where eigenvalues coalesce.
Applications:
•  Exploring non-Hermitian quantum mechanics.
•  Applications in photonics, PT-symmetric systems, and open quantum systems.

Requirements
Hardware
•  General: Laptop (e.g., ThinkPad P73) with webcam, audio output, and Python 3.x.
•  A1: YBCO puck, liquid nitrogen, small magnet, cryogenic PPE.
•  A2: Rewritable DVD, DVD burner, webcam/phone camera.
•  A3: Small speaker (minimal path) or 40 kHz transducer array + driver (levitation path), phone with SPL app.
Software
•  Python 3.x
•  Libraries: numpy, matplotlib, opencv-python (for A2 image analysis), scipy (for simulations).
•  Optional: Jupyter Notebook for plotting.
•  Image analysis tool (e.g., ImageJ) for A2.

Installation
1.  Clone the repository:
git clone https://github.com/yourusername/physics-experiment-suite.git
cd physics-experiment-suite
2.  Install Python
pip install -r requirements.txt
3.  Verify CSV templates are in the /data directory:
	•  EXP_A1_Superconductor_Meissner_Log.csv
	•  EXP_A2_DVD_PhaseChange_Log.csv
	•  EXP_A3_Acoustic_Levitation_Sweep.csv
	•  EXP_Sim_Ising_MonteCarlo_Params.csv
	•  EXP_Sim_PT2x2_Params.csv

Usage
1.  Physical Experiments:
	•  Follow the steps in the Experiments and Simulations section.
	•  Log data in the corresponding CSV files in /data.
2.  Simulations:
	•  Navigate to /simulations/S1_Ising_Model or /simulations/S2_PT_Symmetric.
	•  Edit the parameter CSV files (EXP_Sim_Ising_MonteCarlo_Params.csv or EXP_Sim_PT2x2_Params.csv).
	•  Run the simulation scripts:
python S1_Ising_Model/simulate.py
python S2_PT_Symmetric/simulate.py
3.  Plotting:
	•  Use the provided Jupyter notebooks in /notebooks to visualize results.
	•  Example:
jupyter notebook notebooks/plot_A2_reflectance.ipynb

Data Logging
•  Each experiment/simulation has a dedicated CSV template in /data.
•  Fill in the CSVs during experiments or simulations with the required measurements (e.g., grayscale values for A2, eigenvalues for S2).
•  Ensure consistent units and formatting as specified in the CSV headers.

Plotting and Analysis
To generate plots:
1.  Complete the CSV files with experimental or simulation data.
2.  Run the corresponding Jupyter notebook in /notebooks:
	•  plot_A1_meissner.ipynb: Plots levitation distances.
	•  plot_A2_reflectance.ipynb: Plots reflectance vs. pulse duration.
	•  plot_A3_acoustic.ipynb: Plots node height/stability vs. frequency.
	•  plot_S1_ising.ipynb: Plots magnetization, susceptibility, and heat capacity vs. temperature.
	•  plot_S2_pt_symmetric.ipynb: Plots real/imaginary eigenvalues vs. γ.
Request additional plotting scripts by contacting the maintainer or opening an issue.

Contributing
Contributions are welcome! To contribute:
1.  Fork the repository.
2.  Create a new branch (git checkout -b feature/your-feature).
3.  Commit changes (git commit -m "Add your feature").
4.  Push to the branch (git push origin feature/your-feature).
5.  Open a pull request.
Please include clear documentation and test your changes with the provided CSVs.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Procurement Checklist
For hardware experiments requiring additional materials (e.g., YBCO puck for A1 or transducer array for A3), request a detailed procurement checklist by contacting the maintainer or opening an issue.

Notes
•  Repository Structure:
physics-experiment-suite/
├── data/
│   ├── EXP_A1_Superconductor_Meissner_Log.csv
│   ├── EXP_A2_DVD_PhaseChange_Log.csv
│   ├── EXP_A3_Acoustic_Levitation_Sweep.csv
│   ├── EXP_Sim_Ising_MonteCarlo_Params.csv
│   ├── EXP_Sim_PT2x2_Params.csv
├── simulations/
│   ├── S1_Ising_Model/
│   │   ├── simulate.py
│   ├── S2_PT_Symmetric/
│   │   ├── simulate.py
├── notebooks/
│   ├── plot_A1_meissner.ipynb
│   ├── plot_A2_reflectance.ipynb
│   ├── plot_A3_acoustic.ipynb
│   ├── plot_S1_ising.ipynb
│   ├── plot_S2_pt_symmetric.ipynb
├── requirements.txt
├── README.md
├── LICENSE
•  Customization: Replace yourusername in the clone command with your GitHub username.
•  Plotting: If you want me to generate specific plotting notebooks or Chart.js configurations for any experiment/simulation, let me know the dataset and desired plot type (e.g., line, scatter).
•  Procurement: If you need a detailed procurement list for A1 or A3, I can provide one upon request.
This README is designed to be concise yet comprehensive, making it easy for users to replicate experiments and contribute to the project. Let me know if you need help creating the plotting notebooks or specific code for the simulations!
