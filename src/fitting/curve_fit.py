import numpy as np
from scipy.optimize import curve_fit

def beverton_holt_model(x, R_max, K):
    """
    Beverton-Holt model function for curve fitting.
    
    Parameters:
    x : array-like
        The independent variable (population at time t).
    R_max : float
        The maximum recruitment rate.
    K : float
        The carrying capacity of the environment.
    
    Returns:
    array-like
        The estimated population at time t+1 based on the Beverton-Holt model.
    """
    return (R_max * x) / (1 + (x / K))

def fit_population_data(years, populations):
    """
    Fit the population data to the Beverton-Holt model using curve fitting.
    
    Parameters:
    years : array-like
        The years of the population data.
    populations : array-like
        The observed populations corresponding to the years.
    
    Returns:
    popt : array
        Optimal values for the parameters R_max and K.
    pcov : 2D array
        The estimated covariance of popt.
    """
    # Initial guess for the parameters R_max and K
    initial_guess = [1000, 5000]
    
    # Perform curve fitting
    popt, pcov = curve_fit(beverton_holt_model, populations, populations, p0=initial_guess)
    
    return popt, pcov

def predict_population(initial_population, years, R_max, K):
    """
    Predict future populations using the Beverton-Holt model.
    
    Parameters:
    initial_population : float
        The initial population size.
    years : int
        The number of years to predict.
    R_max : float
        The maximum recruitment rate.
    K : float
        The carrying capacity of the environment.
    
    Returns:
    populations : list
        A list of predicted populations for each year.
    """
    populations = [initial_population]
    
    for _ in range(1, years):
        next_population = beverton_holt_model(populations[-1], R_max, K)
        populations.append(next_population)
    
    return populations