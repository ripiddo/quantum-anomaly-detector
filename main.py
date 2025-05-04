import sys
import os
import argparse
import numpy as np

# Add the src directory to the path to import modules from there
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from quantum.base_anomaly_detector import simulate_tension, create_expected_state, create_anomalous_state, get_statevector, compute_entropy

def print_header():
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   🔬 Quantum Anomaly Detector - Proof of Concept 🧪       ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """)

def main():
    parser = argparse.ArgumentParser(description='Quantum Anomaly Detector')
    parser.add_argument('--no-visualization', action='store_true', help='Run without displaying visualization')
    parser.add_argument('--random', action='store_true', help='Use randomized anomalous states')
    parser.add_argument('--seed', type=int, help='Set random seed for reproducible results')
    args = parser.parse_args()
    
    print_header()
    
    # Set random seed if provided
    if args.seed is not None:
        np.random.seed(args.seed)
        print(f"Random seed set to: {args.seed}")
    
    # Set visualization flag based on args
    os.environ['DISPLAY_VISUALIZATION'] = 'False' if args.no_visualization else 'True'
    
    # Set randomization flag based on args
    os.environ['USE_RANDOM_ANOMALY'] = 'True' if args.random else 'False'
    
    # Run the simulation
    simulate_tension()
    
    print("\n✅ Simulation completed successfully")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())