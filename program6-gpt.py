import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# Differential equation system
def system(t, v):
    x, y = v
    dxdt = y
    dydt = -x + (1 - x**2) * y
    return [dxdt, dydt]

# Plotting the phase space diagram with isoclines
def plot_phase_space():
    # Initial conditions for the phase space
    initial_conditions = [(3, 3), (-2, 2), (0.1, 0.1), (0.5, 1)]
    t_span = (0, 30)
    t_eval = np.linspace(t_span[0], t_span[1], 1000)

    fig, ax = plt.subplots(figsize=(8, 6))

    # Solve and plot the trajectories for different initial conditions
    for x0, y0 in initial_conditions:
        sol = solve_ivp(system, t_span, [x0, y0], t_eval=t_eval)
        x, y = sol.y
        ax.plot(x, y, label=f"x0={x0}, y0={y0}")

    # Compute and plot x-isocline (y = 0)
    x_vals = np.linspace(-3, 3, 400)
    y_isocline = x_vals / (1 - x_vals**2)
    ax.plot(x_vals, np.zeros_like(x_vals), 'r--', label="x-isocline (y = 0)")

    # Compute and plot y-isocline (y = x / (1 - x^2))
    valid = (x_vals > -1) & (x_vals < 1)  # Valid region to avoid singularity at x = ±1
    ax.plot(x_vals[valid], y_isocline[valid], 'b--', label="y-isocline")

    # Set up plot limits, labels, and title
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_xlabel('x (Rabbits)')
    ax.set_ylabel('y (Foxes)')
    ax.set_title('Phase Space with x- and y-Isoclines')

    # Add a legend
    ax.legend()

    # Show the plot
    plt.show()

# Run the plotting function
plot_phase_space()
