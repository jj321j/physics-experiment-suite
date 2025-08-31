
A-LEVEL DESKTOP EXPERIMENTS — QUICKSTART (ThinkPad P73 Ready)

You can run three physical demos with minimal add-ons and two GPU-friendly simulations.
This README outlines protocols and how to use the provided CSV templates.

HARDWARE-LITE PHYSICAL EXPERIMENTS
----------------------------------
A2) Phase-Change on Rewritable DVD (GST material, laptop-only)
   Concept: Rewritable DVDs use a phase-change layer. A DVD burner toggles crystalline/amorphous states.
   What you measure: Reflectivity change via webcam or phone camera + image grayscale.
   Steps:
     1) Use a RW DVD. Burn small test patterns (e.g., 1x1 cm blocks) at various power/pulse settings.
     2) Before/after each burn, take a photo under the same lighting and angle. Load into any image tool, sample grayscale.
     3) Log in EXP_A2_DVD_PhaseChange_Log.csv: power, pulse, grayscale before/after. Compute reflectance_ratio.
     4) Outcome: Plot reflectance vs pulse; identify "threshold" where phase transition occurs (amorphous<->crystalline).
   Safety: Avoid direct laser exposure from open drives; keep disc in drive.

A3) Acoustic Standing Wave / Levitation (kit suggested)
   Concept: Opposed ultrasonic transducers create nodes; particles can "jump" between nodes (potential wells).
   Minimal path (no levitation): Use laptop audio + small speaker to map room standing waves at ~ 50–300 Hz with a phone SPL app.
   Levitation path: Add a cheap 40 kHz transducer array + driver. Sweep frequency and log node height/stability.
   Log in EXP_A3_Acoustic_Levitation_Sweep.csv.

A1) Superconductor Meissner (optional kit)
   Concept: YBCO puck cooled with liquid nitrogen exhibits zero resistance and expels magnetic field (Meissner), causing a small magnet to levitate.
   Record photos/video and simple distances. Log in EXP_A1_Superconductor_Meissner_Log.csv.
   Safety: Cryogenic PPE; ventilation.

SIMULATIONS (RUN ON LAPTOP)
---------------------------
S1) 2D Ising Model Phase Transition
   Use EXP_Sim_Ising_MonteCarlo_Params.csv to set lattice size and temperature range.
   Observables: Magnetization (M), Susceptibility (chi), Heat capacity (Cv) vs Temperature.
   Expect critical behavior near Tc ~ 2.269 (J/k_B = 1 units).
S2) PT-symmetric 2x2 non-Hermitian dimer
   Use EXP_Sim_PT2x2_Params.csv to sweep gain/loss gamma and plot eigenvalues.
   Expect "exceptional point" where real eigenvalues coalesce and become complex.

NEXT STEPS
----------
1) Fill the CSVs as you run experiments/sims.
2) I can generate plotting notebooks to read these CSVs and output graphs.
3) Ask me for a procurement checklist if you want levitation or superconductivity kits.
