# Tension-Based Quantum Anomaly Detector

## Overview

This project explores a new approach to anomaly detection by simulating **”structural tension”** using quantum circuits. Rather than relying on traditional pattern recognition, this model detects anomalies by measuring changes in **quantum state entropy** and **fidelity**. The approach reflects systems thinking, where anomalies emerge as disruptions in the expected evolution of state.

## Concept

- **System states** are modeled as quantum states.
    
- **Expected behavior** is a stable evolution using Hadamard gates (balanced superposition).
    
- **Anomalies** are simulated by applying disruptive quantum operations (e.g., X gate) that alter the expected state.
    
- **Tension** is detected by comparing:
    
    - **Fidelity**: deviation from expected state
        
    - **Entropy**: disorder or instability in the system
        

This model provides a visual and quantitative method to observe system divergence in real-time.

## Features

- Quantum simulation using Qiskit
    
- Entropy and fidelity calculation to track anomaly impact
    
- CLI-based visual output (bar charts)
    
- Educational, exploratory, and research-aligned code structure
    

## Use Cases

- Cybersecurity: Prototype for future quantum-enhanced anomaly detection systems
    
- Education: Systems thinking + quantum computing fusion
    
- Research: Foundation for structural tension modeling in quantum systems
    

## Installation

```bash
pip install qiskit matplotlib numpy
```

## Usage

Run the main script to simulate both normal and anomalous states:

```bash
python tension_anomaly_detector.py
```

The script will output:

- Fidelity between expected and anomalous states
    
- Entropy values for each state
    
- A bar chart comparing entropy levels
    

## Example Output

```
=== Tension Metrics ===
Fidelity between expected and anomalous state: 0.5000
Expected State Entropy: 1.0000
Anomalous State Entropy: 0.0000
```

## File Structure

```
quantum-tension-anomaly/
├── tension_anomaly_detector.py        # Main simulation script
├── README.md                          # Project overview
├── report/                            # Folder for visual reports and summary
│   └── anomaly_detector_summary.pdf
├── images/                            # Diagrams or output screenshots
```

## Author & Concept

This project is inspired by the concept of **”structural tension”** and its use in anomaly detection. It reflects a deeper philosophical and systemic view of change, disruption, and pattern divergence in complex systems.

For more information or collaboration, please reach out via:
- 📧 Email: sinan.tukek@gmail.com
- 🐱 GitHub: [@ripiddo](https://github.com/ripiddo).