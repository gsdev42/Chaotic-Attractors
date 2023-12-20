import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lorenz_system(t, xyz, sigma, rho, beta):
    x, y, z = xyz
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

def simulate_lorenz(sigma=10, rho=28, beta=8/3, initial_conditions=[0, 1, 20], t_span=(0, 25), num_points=10000):
    t_eval = np.linspace(t_span[0], t_span[1], num_points)

    sol = solve_ivp(
        lorenz_system,
        t_span,
        initial_conditions,
        args=(sigma, rho, beta),
        t_eval=t_eval
    )

    return sol.t, sol.y

def plot_lorenz_attractor(t, xyz):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create a rainbow color map
    colors = plt.cm.rainbow(np.linspace(0, 1, len(t)))

    # Plot the Lorenz attractor with rainbow colors
    ax.scatter(xyz[0], xyz[1], xyz[2], c=colors, marker='.', s=1)

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Lorenz Attractor')
    plt.show()

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
