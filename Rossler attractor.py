import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rossler_attractor(t, xyz, a, b, c):
    x, y, z = xyz
    dxdt = -y - z
    dydt = x + a * y
    dzdt = b + z * (x - c)
    return [dxdt, dydt, dzdt]

def simulate_rossler_attractor(a, b, c, initial_conditions, t_span=(0, 50), num_points=10000):
    t_eval = np.linspace(t_span[0], t_span[1], num_points)

    sol = solve_ivp(
        rossler_attractor,
        t_span,
        initial_conditions,
        args=(a, b, c),
        t_eval=t_eval
    )

    return sol.t, sol.y

def plot_rossler_attractor(t, xyz):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create a rainbow color map
    colors = plt.cm.rainbow(np.linspace(0, 1, len(t)))

    # Plot the Rössler attractor with rainbow colors
    ax.scatter(xyz[0], xyz[1], xyz[2], c=colors, marker='.', s=1)

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Colorful Rössler Attractor')
    plt.show()

if __name__ == "__main__":
    # Set parameters for the Rössler attractor
    a = 0.2
    b = 0.2
    c = 5.7

    # Set initial conditions
    initial_conditions = [0.1, 0.0, 0.0]

    # Simulate Rössler attractor
    t, xyz = simulate_rossler_attractor(a, b, c, initial_conditions)

    # Plot Rössler attractor
    plot_rossler_attractor(t, xyz)
