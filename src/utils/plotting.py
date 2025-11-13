import matplotlib.pyplot as plt
import numpy as np

def plot_population_growth(years, population, title="Dinámica poblacional del atún", xlabel="Año", ylabel="Población estimada"):
    plt.figure(figsize=(10, 6))
    plt.plot(years, population, marker='o', linestyle='-', color='b')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def plot_curve_fit(x_data, y_data, fit_function, params, title="Ajuste de curva", xlabel="X", ylabel="Y"):
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, color='red', label='Datos')
    
    x_fit = np.linspace(min(x_data), max(x_data), 100)
    y_fit = fit_function(x_fit, *params)
    
    plt.plot(x_fit, y_fit, color='blue', label='Ajuste de curva')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()