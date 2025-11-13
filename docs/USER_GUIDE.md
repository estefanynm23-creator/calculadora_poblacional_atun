# USER GUIDE for Tuna Population Calculator

## Introduction
The Tuna Population Calculator is an interactive tool designed to model and analyze the population growth of tuna using the Beverton-Holt model. This guide provides step-by-step instructions on how to install, run, and utilize the application effectively.

## Installation

### Prerequisites
Ensure you have Python 3.7 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository
To get started, clone the repository to your local machine using the following command:
```
git clone https://github.com/yourusername/tuna-population-calculator.git
```

### Install Dependencies
Navigate to the project directory and install the required dependencies using pip:
```
cd tuna-population-calculator
pip install -r requirements.txt
```

## Running the Application
To launch the Tuna Population Calculator, execute the following command in your terminal:
```
python src/main.py
```

## Using the Calculator

### Input Parameters
1. **Initial Population (N0)**: Enter the initial population of tuna.
2. **Maximum Recruitment Rate (R_max)**: Set the maximum recruitment rate for the tuna population.
3. **Carrying Capacity (K)**: Define the carrying capacity of the environment.
4. **Number of Years**: Specify the number of years for the simulation.

### Running the Simulation
After entering the parameters, click the "Run Simulation" button. The application will calculate the estimated population for each year and display the results in a graphical format.

### Viewing Results
The results will be presented in a plot showing the population growth over the specified years. You can also view the numerical results in a table format.

## Curve Fitting
The application includes functionality for numerical curve fitting. You can upload your biological data in CSV format to analyze and fit the model to your data.

### Uploading Data
1. Click on the "Upload Data" button.
2. Select your CSV file containing the biological data.
3. The application will process the data and display the fitted curve alongside the original data points.

## Technical Support
For any issues or questions, please refer to the [Technical Documentation](TECHNICAL.md) or contact the project maintainers.

## Conclusion
The Tuna Population Calculator is a powerful tool for researchers and enthusiasts interested in marine biology and population dynamics. By following this guide, you can effectively utilize the application to model and analyze tuna populations.