import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
# Define the function representing the differential equation
def diff_eqn(y, t, L, R, u, psi_function):
    i, psi = y
    di_dt = (u(t) - R*i - psi_function(psi)) / L
    d_psi_dt = i
    return [di_dt, d_psi_dt]

# Example psi function (you would replace this with your own function)
def psi_function(psi):
    return np.sin(psi)

# Example input voltage function (you would replace this with your own function)
def input_voltage(t):
    return 1.0

# Example parameters
L = 1.0  # Inductance
R = 1.0  # Resistance

# Initial conditions
initial_conditions = [0.0, 0.0]  # Initial current and psi

# Time points to solve the equation at
t = np.linspace(0, 10, 100)  # Example time points

# Solve the differential equation
solution = odeint(diff_eqn, initial_conditions, t, args=(L, R, input_voltage, psi_function))

# Extract the current from the solution
current = solution[:, 0]

# Print or visualize the results as needed
print(current)
plt.plot(current)
plt.show()
