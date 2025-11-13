# Technical Documentation for Tuna Population Calculator

## Overview

The Tuna Population Calculator is an interactive application designed to model and analyze the population growth of tuna using the Beverton-Holt model. The application features a graphical user interface (GUI) that allows users to input parameters, visualize population dynamics, and perform numerical curve fitting on biological data.

## Architecture

The project is structured into several modules, each serving a specific purpose:

- **src/main.py**: The entry point of the application that initializes the GUI.
- **src/gui**: Contains the GUI components and application logic.
  - **app.py**: Main application logic for handling user interactions.
  - **components.py**: Defines reusable GUI components.
- **src/models**: Implements population growth models.
  - **beverton_holt.py**: Contains the Beverton-Holt model functions.
- **src/fitting**: Provides numerical curve fitting methods.
  - **curve_fit.py**: Functions for processing biological data.
- **src/data**: Contains sample data for testing and analysis.
- **src/utils**: Utility functions for I/O operations and plotting.
- **src/types**: Custom types and data structures used throughout the application.

## Design Decisions

1. **Model Selection**: The Beverton-Holt model was chosen for its simplicity and effectiveness in modeling fish population dynamics. It allows for the estimation of future populations based on current data and environmental capacity.

2. **GUI Framework**: The application uses a user-friendly GUI framework to facilitate user interaction. This design choice enhances accessibility for users with varying levels of technical expertise.

3. **Modular Structure**: The project is organized into distinct modules to promote code reusability and maintainability. Each module focuses on a specific aspect of the application, making it easier to manage and extend.

4. **Data Handling**: Sample biological data is stored in CSV format, allowing for easy integration and analysis. Utility functions are provided for reading and processing this data.

## Implementation Details

### Beverton-Holt Model

The Beverton-Holt model is implemented in `src/models/beverton_holt.py`. The key function is:

```python
def beverton_holt(N, R_max, K):
    """
    Calculates the next population size using the Beverton-Holt model.
    N: Current population size
    R_max: Maximum recruitment rate
    K: Carrying capacity of the environment
    """
    N_next = (R_max * N) / (1 + (N / K))
    return N_next
```

### Curve Fitting

Numerical curve fitting methods are implemented in `src/fitting/curve_fit.py`. These methods allow users to fit biological data to the Beverton-Holt model, providing insights into population dynamics.

### GUI Components

The GUI is built using components defined in `src/gui/components.py`. This modular approach allows for easy updates and enhancements to the user interface.

## Testing

Unit tests are provided in the `tests` directory to ensure the correctness of the model and fitting functions. These tests validate that the implemented algorithms produce expected results under various scenarios.

## Conclusion

The Tuna Population Calculator is a comprehensive tool for modeling tuna population growth. Its modular design, user-friendly interface, and robust data handling capabilities make it a valuable resource for researchers and practitioners in marine biology and fisheries management.