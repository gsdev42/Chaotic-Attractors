# Chaotic-Attractors
 Simulating Rössler attractor and the Lorenz attractor

# Lorenz Attractor Simulation

This Python script generates and visualizes the Lorenz attractor, a famous example of a chaotic dynamical system. The Lorenz system is described by a set of three coupled ordinary differential equations, and it exhibits intricate and unpredictable behavior over time.

## Prerequisites

Make sure you have the required dependencies installed. You can install them using:

```bash
pip install numpy scipy matplotlib
```

### Code Overview
The code is organized into three main functions:

## lorenz_system(t, xyz, sigma, rho, beta):

Defines the Lorenz system of differential equations.
Parameters:
t: Time variable.
xyz: Current state vector [x, y, z].
sigma, rho, beta: System parameters.
Returns the rate of change of each variable.


## simulate_lorenz(sigma, rho, beta, initial_conditions, t_span, num_points):

Uses SciPy's solve_ivp to numerically solve the Lorenz system.
Parameters:
sigma, rho, beta: System parameters.
initial_conditions: Initial values for [x, y, z].
t_span: Time span for simulation.
num_points: Number of points for time discretization.
Returns time values and the state trajectory.


## plot_lorenz_attractor(t, xyz):

Plots the Lorenz attractor in 3D using Matplotlib.
Uses a rainbow color map to add visual appeal.
Parameters:
t: Time values.
xyz: State trajectory.



### Main Block

```python
if __name__ == "__main__":
    # Set parameters and initial conditions
    sigma = 10
    rho = 28
    beta = 8/3
    initial_conditions = [0, 1, 20]

    # Simulate Lorenz attractor
    t, xyz = simulate_lorenz(sigma, rho, beta, initial_conditions)

    # Plot colorful Lorenz attractor
    plot_lorenz_attractor(t, xyz)
```

## Usage

1. Run the script by executing the following command:

    ```bash
    python lorenz_attractor.py
    ```

2. The script will simulate the Lorenz attractor and display a 3D plot with rainbow-colored trajectories.

Feel free to experiment with different parameters and initial conditions to observe the impact on the Lorenz attractor's behavior.
