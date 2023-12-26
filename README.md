# Chaotic-Attractors
 Simulating Rössler attractor and the Lorenz attractor

# Lorenz Attractor Simulation

The Lorenz system is chaotic dynamical system described by a set of three coupled ordinary differential equations, and it exhibits unpredictable behavior over time.

<img width="274" alt="image" src="https://github.com/garima-sagar/Chaotic-Attractors/assets/145219684/f5893f64-edcd-49e7-bff6-4d155f41b26a">


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

_______________________________________________________________________________________________________
_______________________________________________________________________________________________________

# Rossler Attractor

# Rössler Attractor Simulation

The Rössler system is described by three coupled nonlinear differential equations that exhibit chaotic behavior characterized by interesting trajectories in three-dimensional space.

<img width="289" alt="image" src="https://github.com/garima-sagar/Chaotic-Attractors/assets/145219684/9e63a61c-db25-4739-9807-746799622ad7">


## Code Overview

The code consists of three main functions:

1. **rossler_attractor(t, xyz, a, b, c):**
   - Defines the Rössler system of differential equations.
   - Parameters:
     - `t`: Time variable.
     - `xyz`: Current state vector [x, y, z].
     - `a`, `b`, `c`: System parameters.
   - Returns the rate of change of each variable.

2. **simulate_rossler_attractor(a, b, c, initial_conditions, t_span, num_points):**
   - Uses SciPy's `solve_ivp` to numerically solve the Rössler system.
   - Parameters:
     - `a`, `b`, `c`: System parameters.
     - `initial_conditions`: Initial values for [x, y, z].
     - `t_span`: Time span for simulation.
     - `num_points`: Number of points for time discretization.
   - Returns time values and the state trajectory.

3. **plot_rossler_attractor(t, xyz):**
   - Plots the Rössler attractor in 3D using Matplotlib.
   - Uses a rainbow color map to add visual appeal.
   - Parameters:
     - `t`: Time values.
     - `xyz`: State trajectory.

## Usage

1. Set the parameters and initial conditions in the `__main__` block.
2. Run the script.
3. The simulation results are displayed in a 3D plot showing the evolution of the Rössler attractor over time.

## Dependencies

- `numpy`: For numerical operations.
- `scipy`: For solving differential equations using `solve_ivp`.
- `matplotlib`: For creating 3D visualizations.

## Example

```python
if __name__ == "__main__":
    # Set parameters for the Rössler attractor
    a = 0.2
    b = 0.2
    c = 5.7

    # Set initial conditions
    initial_conditions = [0.1, 0.0, 0.0]

    # Simulate Rössler attractor
    t, xyz = simulate_rossler_attractor(a, b, c, initial_conditions)

    # Plot colorful Rössler attractor
    plot_rossler_attractor(t, xyz)
```

Feel free to experiment with different parameter values and initial conditions to observe the impact on the Rössler attractor's behavior. Contributions and improvements are welcome!
