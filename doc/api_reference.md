# Quantum Anomaly Detector: API Reference

This document provides detailed information about the functions and modules in the Quantum Anomaly Detector for developers who want to integrate with or extend its functionality.

## Module Structure

```
quantum-anomaly-detector/
├── main.py                      # Main entry point
└── src/                         # Source code
    └── quantum/                 # Quantum computing components
        └── base_anomaly_detector.py  # Core quantum functionality
```

## Core Functions

### main.py

#### `main()`
Entry point for the application, handles command-line arguments and initiates simulation.

**Parameters:** None (uses command-line arguments)  
**Returns:** Integer status code (0 for success)

#### `print_header()`
Displays the application header in the terminal.

**Parameters:** None  
**Returns:** None

### src/quantum/base_anomaly_detector.py

#### `create_expected_state()`
Creates a quantum circuit representing the expected system state.

**Parameters:** None  
**Returns:** `QuantumCircuit` - A Qiskit quantum circuit with a balanced superposition state

```python
# Example usage
expected_circuit = create_expected_state()
```

#### `create_anomalous_state()`
Creates a quantum circuit representing an anomalous system state.

**Parameters:** None (uses environment variables for configuration)  
**Returns:** `QuantumCircuit` - A Qiskit quantum circuit with an anomalous state

**Environment Variables:**
- `USE_RANDOM_ANOMALY`: If 'True', generates randomized anomalies

```python
# Example usage
anomalous_circuit = create_anomalous_state()
```

#### `get_statevector(qc)`
Extracts the statevector from a quantum circuit.

**Parameters:**
- `qc`: `QuantumCircuit` - The quantum circuit to simulate

**Returns:** `Statevector` - The resulting quantum state vector

```python
# Example usage
sv = get_statevector(quantum_circuit)
```

#### `compute_entropy(statevector)`
Computes the entropy of a quantum state.

**Parameters:**
- `statevector`: `Statevector` - The quantum state vector

**Returns:** `float` - The entropy value

```python
# Example usage
entropy = compute_entropy(state_vector)
```

#### `simulate_tension()`
Main function that simulates both expected and anomalous states and computes comparison metrics.

**Parameters:** None (uses environment variables for configuration)  
**Returns:** None (displays results and optionally shows visualization)

**Environment Variables:**
- `DISPLAY_VISUALIZATION`: If not 'False', displays visualization plots
- `USE_RANDOM_ANOMALY`: If 'True', uses randomized anomalous states

```python
# Example usage
simulate_tension()
```

## Command-line Arguments

The application accepts the following command-line arguments:

| Argument | Description |
|----------|-------------|
| `--no-visualization` | Run without displaying visualization |
| `--random` | Use randomized anomalous states |
| `--seed <INT>` | Set random seed for reproducible results |

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DISPLAY_VISUALIZATION` | Controls whether visualization is displayed | 'True' |
| `USE_RANDOM_ANOMALY` | Controls whether random anomalies are used | 'False' |

## Integration Examples

### Basic Integration

```python
import os
from quantum.base_anomaly_detector import simulate_tension

# Configure environment
os.environ['DISPLAY_VISUALIZATION'] = 'True'
os.environ['USE_RANDOM_ANOMALY'] = 'False'

# Run simulation
simulate_tension()
```

### Custom Anomaly Detection

```python
import numpy as np
from quantum.base_anomaly_detector import create_expected_state, get_statevector, compute_entropy
from qiskit import QuantumCircuit
from qiskit.quantum_info import state_fidelity

# Create expected state
expected_qc = create_expected_state()
sv_expected = get_statevector(expected_qc)

# Create custom anomaly detector
def detect_custom_anomaly(custom_circuit):
    # Get state vector from custom circuit
    sv_custom = get_statevector(custom_circuit)
    
    # Compute metrics
    fidelity = state_fidelity(sv_expected, sv_custom)
    entropy_expected = compute_entropy(sv_expected)
    entropy_custom = compute_entropy(sv_custom)
    severity = 1.0 - fidelity
    
    # Determine anomaly severity
    if severity < 0.3:
        status = "LOW"
    elif severity < 0.7:
        status = "MEDIUM"
    else:
        status = "HIGH"
    
    return {
        "fidelity": fidelity,
        "entropy_expected": entropy_expected,
        "entropy_custom": entropy_custom,
        "severity": severity,
        "status": status
    }

# Example custom circuit
custom_qc = QuantumCircuit(1)
custom_qc.ry(np.pi/4, 0)

# Detect anomaly
results = detect_custom_anomaly(custom_qc)
print(f"Anomaly Status: {results['status']}")
```

## Extension Points

The system can be extended in several ways:

1. **Custom Anomaly Generators**: Modify or replace `create_anomalous_state()` to generate different types of anomalies

2. **Additional Metrics**: Add new quantum metrics beyond fidelity and entropy

3. **Multi-qubit Systems**: Extend the implementation to use multiple qubits for more complex analysis

4. **Alternative Visualizations**: Enhance or replace the visualization code in `simulate_tension()`

## Dependencies

- **Qiskit**: For quantum circuit creation and simulation
- **NumPy**: For mathematical operations
- **Matplotlib**: For visualization