import numpy as np

def beverton_holt(N, R_max, K):
    """
    Calculates the population at the next time step using the Beverton-Holt model.
    
    Parameters:
    N (float): Current population
    R_max (float): Maximum recruitment rate
    K (float): Carrying capacity of the environment
    
    Returns:
    float: Estimated population at the next time step
    """
    N_next = (R_max * N) / (1 + (N / K))
    return N_next

def simulate_population_growth(N0, R_max, K, n_years):
    """
    Simulates the population growth over a specified number of years.
    
    Parameters:
    N0 (float): Initial population
    R_max (float): Maximum recruitment rate
    K (float): Carrying capacity of the environment
    n_years (int): Number of years to simulate
    
    Returns:
    np.ndarray: Array of population estimates for each year
    """
    population = np.zeros(n_years)
    population[0] = N0

    for t in range(1, n_years):
        population[t] = beverton_holt(population[t-1], R_max, K)

    return population