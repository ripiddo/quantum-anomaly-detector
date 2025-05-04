# Quantum Anomaly Detector: Technical Details

This document provides an in-depth explanation of the quantum computing principles and implementation details of the Quantum Anomaly Detector.

## Table of Contents
1. [Quantum Computing Fundamentals](#quantum-computing-fundamentals)
2. [Quantum States in Anomaly Detection](#quantum-states-in-anomaly-detection)
3. [Implementation Details](#implementation-details)
4. [Metrics and Analysis](#metrics-and-analysis)
5. [Visualization](#visualization)
6. [Future Enhancements](#future-enhancements)

## Quantum Computing Fundamentals

### Qubits and Superposition

Unlike classical bits that can only be in states 0 or 1, quantum bits (qubits) can exist in a superposition of both states simultaneously. This property is leveraged in our anomaly detector to represent complex system states.

A qubit in superposition is represented as:

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$$

Where $\alpha$ and $\beta$ are complex amplitudes, and $|\alpha|^2 + |\beta|^2 = 1$

### Quantum Gates

Our implementation uses several quantum gates:
- **Hadamard (H) Gate**: Creates a superposition state
- **Pauli-X Gate**: Flips the state of a qubit (quantum equivalent of a NOT gate)
- **Rotation Gates** (Rx, Ry, Rz): Rotate the qubit state around the X, Y, and Z axes of the Bloch sphere

## Quantum States in Anomaly Detection

### Expected State

The expected state in our system is created using a Hadamard gate, which puts the qubit in an equal superposition:

```python
def create_expected_state():
    qc = QuantumCircuit(1)
    qc.h(0)  # Hadamard gate for balanced superposition
    return qc
```

This produces the state:

$$|\psi_{expected}\rangle = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle$$

### Anomalous State

Anomalous states are created either:
1. Using a deterministic approach (X gate):
   
   $$|\psi_{anomalous}\rangle = |1\rangle$$

2. Or through randomized rotations (when the `--random` flag is used):
   
   ```python
   theta = np.random.uniform(0, np.pi)
   phi = np.random.uniform(0, 2*np.pi)
   lam = np.random.uniform(0, np.pi/2)
   
   qc.ry(theta, 0)
   qc.rz(phi, 0)
   qc.rx(lam, 0)
   ```

   This creates diverse anomalous states with varying probability distributions.

## Implementation Details

### Core Components

The system is built on Qiskit, IBM's open-source quantum computing framework, and uses the following key components:

1. **Quantum Circuit Creation**: Definition of quantum circuits for expected and anomalous states
2. **State Vector Simulation**: Using Qiskit's `statevector_simulator` backend
3. **Metric Computation**: Calculation of fidelity and entropy
4. **Anomaly Analysis**: Severity classification based on state divergence

### Code Architecture

The implementation follows a modular design:
- `main.py`: Entry point with command-line argument handling
- `base_anomaly_detector.py`: Core quantum functionality

## Metrics and Analysis

### Fidelity

State fidelity measures the "closeness" of two quantum states. A fidelity of 1 means identical states, while 0 means orthogonal states.

$$F(|\psi\rangle, |\phi\rangle) = |\langle\psi|\phi\rangle|^2$$

In our implementation, fidelity is calculated using Qiskit's `state_fidelity` function.

### Entropy

Von Neumann entropy quantifies the uncertainty in a quantum state. For a state with probabilities derived from amplitudes:

$$S(\rho) = -\sum_i p_i \log_2 p_i$$

Where $p_i = |\alpha_i|^2$ for each basis state.

### Anomaly Severity Classification

Anomaly severity is determined based on the fidelity between expected and anomalous states:

```
severity = 1.0 - fidelity

if severity < 0.3:
    status = "LOW"
elif severity < 0.7:
    status = "MEDIUM"
else:
    status = "HIGH"
```

## Visualization

When visualization is enabled, the system generates:

1. **Entropy Comparison**: Bar chart showing entropy values for expected and anomalous states
2. **Fidelity/Severity Plot**: Stacked bar chart showing fidelity and severity with threshold indicators

## Future Enhancements

Potential areas for improvement include:

1. **Multi-Qubit Systems**: Extending to multiple qubits for more complex system representation
2. **Quantum Machine Learning**: Incorporating quantum machine learning techniques for adaptive anomaly detection
3. **Real-time Monitoring**: Implementing a continuous monitoring system for real-time anomaly detection
4. **Noise Simulation**: Adding realistic quantum noise models to test detector robustness
5. **Hardware Execution**: Running on actual quantum hardware instead of simulation

## References

1. Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*.
2. Qiskit Documentation - [https://qiskit.org/documentation/](https://qiskit.org/documentation/)
3. "Quantum Machine Learning for Data Classification" - Schuld, M., Sinayskiy, I., & Petruccione, F. (2015).