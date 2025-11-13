from tkinter import Frame, Label, Entry, Button, StringVar, messagebox
import matplotlib.pyplot as plt

class PopulationCalculatorComponents(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, text="Tuna Population Calculator", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.initial_population_label = Label(self, text="Initial Population:")
        self.initial_population_label.pack()
        self.initial_population = StringVar()
        self.initial_population_entry = Entry(self, textvariable=self.initial_population)
        self.initial_population_entry.pack(pady=5)

        self.max_recruitment_label = Label(self, text="Max Recruitment Rate:")
        self.max_recruitment_label.pack()
        self.max_recruitment = StringVar()
        self.max_recruitment_entry = Entry(self, textvariable=self.max_recruitment)
        self.max_recruitment_entry.pack(pady=5)

        self.carrying_capacity_label = Label(self, text="Carrying Capacity:")
        self.carrying_capacity_label.pack()
        self.carrying_capacity = StringVar()
        self.carrying_capacity_entry = Entry(self, textvariable=self.carrying_capacity)
        self.carrying_capacity_entry.pack(pady=5)

        self.simulate_button = Button(self, text="Simulate", command=self.simulate_population)
        self.simulate_button.pack(pady=10)

        self.quit_button = Button(self, text="Quit", command=self.master.quit)
        self.quit_button.pack(pady=5)

    def simulate_population(self):
        try:
            N0 = float(self.initial_population.get())
            R_max = float(self.max_recruitment.get())
            K = float(self.carrying_capacity.get())
            n_years = 50

            population = [N0]
            for t in range(1, n_years):
                N_next = (R_max * population[t-1]) / (1 + (population[t-1] / K))
                population.append(N_next)

            self.plot_population(population)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")

    def plot_population(self, population):
        plt.figure(figsize=(10, 5))
        plt.plot(range(len(population)), population, marker='o')
        plt.title("Tuna Population Growth Simulation")
        plt.xlabel("Years")
        plt.ylabel("Population")
        plt.grid(True)
        plt.show()