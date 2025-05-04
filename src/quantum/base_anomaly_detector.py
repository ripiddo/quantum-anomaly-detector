from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.quantum_info import state_fidelity
import numpy as np
import matplotlib.pyplot as plt
import os

# Create expected system state (neutral, balanced)
def create_expected_state():
    qc = QuantumCircuit(1)
    qc.h(0)  # Hadamard gate for balanced superposition
    return qc

# Create anomalous system state (strong asymmetry)
def create_anomalous_state():
    qc = QuantumCircuit(1)
    
    # Check if random anomalies are enabled
    if os.environ.get('USE_RANDOM_ANOMALY', 'False').lower() == 'true':
        # Random rotation angle creates different anomalies each run
        # Add more randomness by using a more complex distribution
        theta = np.random.uniform(0, np.pi)
        phi = np.random.uniform(0, 2*np.pi)
        lam = np.random.uniform(0, np.pi/2)  # Additional randomization parameter
        
        # Apply multiple rotation gates for more diverse states
        qc.ry(theta, 0)  # Rotation around Y axis
        qc.rz(phi, 0)    # Rotation around Z axis
        qc.rx(lam, 0)    # Rotation around X axis for additional variation
        
        print(f"Generated random anomaly with parameters: theta={theta:.4f}, phi={phi:.4f}, lambda={lam:.4f}")
    else:
        # Default deterministic anomaly
        qc.x(0)  # X gate to simulate unexpected disruption
    
    return qc

# Extract statevector from quantum circuit
def get_statevector(qc):
    backend = Aer.get_backend('statevector_simulator')
    job = backend.run(qc)
    result = job.result()
    return result.get_statevector()

# Compute entropy of a quantum state
def compute_entropy(statevector):
    probs = np.abs(statevector.data) ** 2
    return -np.sum(probs * np.log2(probs + 1e-10))

# Simulate both paths and compute tension metrics
def simulate_tension():
    expected_qc = create_expected_state()
    anomalous_qc = create_anomalous_state()

    sv_expected = get_statevector(expected_qc)
    sv_anomalous = get_statevector(anomalous_qc)

    fid = state_fidelity(sv_expected, sv_anomalous)
    entropy_expected = compute_entropy(sv_expected)
    entropy_anomalous = compute_entropy(sv_anomalous)

    print("=== Tension Metrics ===")
    print(f"Fidelity between expected and anomalous state: {fid:.4f}")
    print(f"Expected State Entropy: {entropy_expected:.4f}")
    print(f"Anomalous State Entropy: {entropy_anomalous:.4f}")
    
    # Determine anomaly severity
    severity = 1.0 - fid
    if severity < 0.3:
        status = "LOW"
    elif severity < 0.7:
        status = "MEDIUM"
    else:
        status = "HIGH"
    
    print(f"Anomaly Severity: {severity:.4f} - Status: {status}")

    # Plot entropy difference if visualization is enabled
    if os.environ.get('DISPLAY_VISUALIZATION') != 'False':
        # Create figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Entropy comparison plot
        labels = ['Expected', 'Anomalous']
        values = [entropy_expected, entropy_anomalous]
        ax1.bar(labels, values, color=['skyblue', 'salmon'])
        ax1.set_title('Entropy Comparison')
        ax1.set_ylabel('Entropy')
        ax1.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Fidelity/Severity plot
        severity_data = [severity]
        fidelity_data = [fid]
        x = ['Quantum State']
        
        ax2.bar(x, fidelity_data, label='Fidelity', color='green', alpha=0.6)
        ax2.bar(x, severity_data, bottom=fidelity_data, label='Severity', color='red', alpha=0.6)
        ax2.axhline(y=0.7, color='red', linestyle='--', alpha=0.5, label='High Severity Threshold')
        ax2.axhline(y=0.3, color='orange', linestyle='--', alpha=0.5, label='Medium Severity Threshold')
        ax2.set_ylim(0, 1.0)
        ax2.set_title('Anomaly Analysis')
        ax2.set_ylabel('Measurement')
        ax2.legend(loc='upper right')
        ax2.grid(axis='y', linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Set default environment variables when run directly
    if 'DISPLAY_VISUALIZATION' not in os.environ:
        os.environ['DISPLAY_VISUALIZATION'] = 'True'
    if 'USE_RANDOM_ANOMALY' not in os.environ:
        os.environ['USE_RANDOM_ANOMALY'] = 'False'
        
    simulate_tension()
