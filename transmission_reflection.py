import numpy as np

# Parameters:

# Intrinsic impedances
Z1, Z2 = 50, 75  # Ohms
# Angles
theta1, theta2 = 0, 0  # Radians

# Parallel polarization

# Reflection coefficient
Gamma_parallel = (Z2 * np.cos(theta2) - Z1 * np.cos(theta1)) / (Z2 * np.cos(theta2) + Z1 * np.cos(theta1))
# Transmission coefficient
T_parallel = (2 * Z2 * np.cos(theta1)) / (Z2 * np.cos(theta2) + Z1 * np.cos(theta1))