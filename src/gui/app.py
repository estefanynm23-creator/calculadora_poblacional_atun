import sys
from pathlib import Path

# Ensure project `src` is on sys.path so imports like `models.*` work
ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from models.beverton_holt import beverton_holt
from fitting.curve_fit import fit_population_data

class TunaPopulationCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tuna Population Calculator")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Input frame
        input_frame = ttk.LabelFrame(self.root, text="Input Parameters")
        input_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(input_frame, text="Initial Population (N0):").grid(row=0, column=0, padx=5, pady=5)
        self.n0_entry = ttk.Entry(input_frame)
        self.n0_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Max Recruitment Rate (R_max):").grid(row=1, column=0, padx=5, pady=5)
        self.r_max_entry = ttk.Entry(input_frame)
        self.r_max_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Carrying Capacity (K):").grid(row=2, column=0, padx=5, pady=5)
        self.k_entry = ttk.Entry(input_frame)
        self.k_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Number of Years:").grid(row=3, column=0, padx=5, pady=5)
        self.years_entry = ttk.Entry(input_frame)
        self.years_entry.grid(row=3, column=1, padx=5, pady=5)

        # Calculate button
        self.calculate_button = ttk.Button(self.root, text="Calculate Population", command=self.calculate_population)
        self.calculate_button.grid(row=1, column=0, padx=10, pady=10)

        # Output frame
        self.output_frame = ttk.LabelFrame(self.root, text="Population Results")
        self.output_frame.grid(row=2, column=0, padx=10, pady=10)

        self.results_text = tk.Text(self.output_frame, width=50, height=15)
        self.results_text.grid(row=0, column=0, padx=5, pady=5)

    def calculate_population(self):
        try:
            # allow floats for rates and capacity
            N0 = float(self.n0_entry.get())
            R_max = float(self.r_max_entry.get())
            K = float(self.k_entry.get())
            n_years = int(float(self.years_entry.get()))

            population = np.zeros(n_years)
            population[0] = N0

            for t in range(1, n_years):
                population[t] = beverton_holt(population[t-1], R_max, K)

            self.display_results(population)
            self.plot_population(population)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")

    def display_results(self, population):
        self.results_text.delete(1.0, tk.END)
        for year, pop in enumerate(population):
            self.results_text.insert(tk.END, f"Año {year}: Población estimada = {pop:.2f}\n")

    def plot_population(self, population):
        plt.figure()
        plt.plot(range(len(population)), population)
        plt.title("Dinámica poblacional del atún (Modelo Beverton-Holt)")
        plt.xlabel("Año")
        plt.ylabel("Población estimada")
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = TunaPopulationCalculatorApp(root)
    root.mainloop()