# Quantum Anomaly Detector: User Guide

This guide provides practical instructions for using the Quantum Anomaly Detector, aimed at users who may not have extensive quantum computing knowledge.

## Getting Started

### Prerequisites

Before using the Quantum Anomaly Detector, ensure you have:

1. Python 3.8 or later installed
2. Required Python packages installed:
   - Qiskit and Qiskit-Aer
   - NumPy
   - Matplotlib

You can install all prerequisites with:
```
pip install qiskit qiskit-aer numpy matplotlib
```

### Quick Start

1. Open a terminal and navigate to the project directory
2. Run the detector with default settings:
   ```
   python main.py
   ```
3. View the results in the terminal and any visualization that appears

## Common Use Cases

### Basic Anomaly Detection

For standard anomaly detection with visualization:
```
python main.py
```

The system will:
- Create an expected quantum state (balanced)
- Create a deterministic anomalous state (using X gate)
- Calculate fidelity and entropy metrics
- Display the results with visualization

### Random Anomaly Simulation

To test with random anomalous states:
```
python main.py --random
```

Each run will generate different anomalies with varying severity levels, useful for:
- Testing detector sensitivity
- Exploring different types of quantum anomalies
- Visualizing how different anomalies affect entropy and fidelity

### Reproducible Testing

For consistent results (especially with random anomalies):
```
python main.py --random --seed 42
```

Use the same seed number to reproduce identical results across multiple runs.

### Headless Mode

For running without visualization (useful in automated scripts):
```
python main.py --no-visualization
```

## Understanding the Output

### Terminal Output

The program displays:
```
=== Tension Metrics ===
Fidelity between expected and anomalous state: 0.0000
Expected State Entropy: 1.0000
Anomalous State Entropy: 0.0000
Anomaly Severity: 1.0000 - Status: HIGH
```

Key metrics explained:
- **Fidelity**: Similarity between expected and anomalous states (1.0 = identical, 0.0 = completely different)
- **Entropy**: Uncertainty in the quantum state
- **Anomaly Severity**: Calculated as 1.0 - fidelity
- **Status**: Classification of severity (LOW, MEDIUM, HIGH)

### Visualization

When enabled, the program generates two plots:

1. **Entropy Comparison**:
   - Blue bar: Expected state entropy
   - Red bar: Anomalous state entropy
   - Larger differences indicate stronger anomalies

2. **Anomaly Analysis**:
   - Green section: Fidelity (similarity to expected state)
   - Red section: Severity (difference from expected state)
   - Dashed lines: Threshold values for severity classification

## Troubleshooting

### Common Issues

1. **Missing Dependencies**:
   ```
   ModuleNotFoundError: No module named 'qiskit'
   ```
   Solution: Install required packages with `pip install qiskit qiskit-aer numpy matplotlib`

2. **Visualization Not Appearing**:
   - Check that you haven't used the `--no-visualization` flag
   - Ensure matplotlib is properly installed
   - Try running in a different environment if using remote connections

3. **Random Seed Not Working**:
   - Ensure you're providing an integer value: `--seed 42`
   - Verify that the same command produces the same output when repeated

## Advanced Usage

### Custom Anomaly Patterns

The system can be extended to create custom anomalous states by modifying the `create_anomalous_state()` function in `src/quantum/base_anomaly_detector.py`.

### Integration with Other Systems

Output can be captured and integrated with other monitoring systems by:
1. Running in headless mode (`--no-visualization`)
2. Parsing the terminal output
3. Using the severity metrics for alerting or further analysis

## Next Steps

After getting familiar with the basic operation:
1. Read the [Technical Documentation](technical_details.md) for deeper understanding
2. Explore the summary report in the `report` directory
3. Consider the [Future Enhancements](technical_details.md#future-enhancements) section for potential project extensions