# Quantum Anomaly Detector

A proof-of-concept implementation of quantum computing techniques for anomaly detection in complex systems.

## Overview

The Quantum Anomaly Detector leverages quantum computing principles to identify deviations from expected system states. By analyzing quantum state entropy and fidelity metrics, the detector can identify anomalous behavior with varying degrees of severity.

## Features

- Quantum state simulation using Qiskit
- Entropy-based anomaly detection 
- Fidelity comparison between expected and anomalous states
- Customizable anomaly severity thresholds
- Visualization of entropy differences and anomaly severity
- Support for randomized anomalous states

## Requirements

- Python 3.8+
- Qiskit
- NumPy
- Matplotlib

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/quantum-anomaly-detector.git
   cd quantum-anomaly-detector
   ```

2. Install the required dependencies:
   ```
   pip install qiskit qiskit-aer numpy matplotlib
   ```

## Usage

Run the anomaly detector with default settings:
```
python main.py
```

### Command Line Arguments

- `--no-visualization`: Run without displaying visualization plots
- `--random`: Use randomized anomalous states for more diverse anomaly patterns
- `--seed <INT>`: Set random seed for reproducible results

### Example

```
python main.py --random --seed 42
```

## How It Works

The detector operates by:
1. Creating an expected quantum state (balanced superposition)
2. Generating an anomalous state (either predetermined or randomized)
3. Computing quantum state metrics (fidelity and entropy)
4. Determining anomaly severity based on the deviation from expected state

For more details, see the [technical documentation](doc/technical_details.md).

## Project Structure

```
quantum-anomaly-detector/
├── main.py               # Main application entry point
├── README.md             # This file
├── doc/                  # Documentation
│   └── technical_details.md
├── images/               # Images for documentation
├── report/               # Analysis reports
│   └── anomaly_detector_summary.pdf
└── src/                  # Source code
    └── quantum/          # Quantum computing components
        └── base_anomaly_detector.py
```

## License

MIT

## Acknowledgments

- [Qiskit](https://qiskit.org/) - Quantum computing framework
- [Quantum Information Science](https://qiskit.org/textbook/ch-ex/hello-qiskit.html) - Educational resources
