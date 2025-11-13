import numpy as np
import pandas as pd
from fitting.curve_fit import fit_curve

def test_fit_curve():
    # Sample data for testing
    years = np.array([0, 1, 2, 3, 4, 5])
    populations = np.array([500, 800, 1200, 1800, 2500, 3000])
    
    # Fit the curve using the fitting function
    params = fit_curve(years, populations)
    
    # Check if the parameters are returned correctly
    assert params is not None, "Parameters should not be None"
    assert len(params) == 3, "Expected 3 parameters for the curve fit"
    
    # Validate the fitted parameters (example checks)
    assert params[0] > 0, "R_max should be positive"
    assert params[1] > 0, "K should be positive"
    assert params[2] >= 0, "Initial population N0 should be non-negative"

def run_tests():
    test_fit_curve()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()