

"""

This is the main run file

"""

# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from averagefunction import average_values
from Bin_average_function import bin_average_velocities
from vorticity_fluctuations_KE_functions import Vorticity, Velocity_fluctuations, Turbulent_kinetic_energy
from Vorticity_image_gen import Vorticity_image, Velocity_fluctuations_image

# Select the plane of interest and propeller configuration.


# Extract the data

    # Obtain unsteady flow field

    # Convert into time averaged flow fields

    
average_U_arr, average_V_arr = average_values(1, 4000, 'B', 1)

    # Convert into bin averaged flow fields
for i in range(1, 36):
    u_magnitudes, v_magnitudes = bin_average_velocities(i, 'B', 1)


# Obtain the flow properties for bin averaged flow fields and plot the flow properties / Visualize
    Vorticity_image(u_magnitudes, v_magnitudes, 'B', 1, i)

    Velocity_fluctuations_image(u_magnitudes, v_magnitudes, average_U_arr, average_V_arr, 'B', 1, i)
"""Velocity_fluctuations_u, Velocity_fluctuations_v = Velocity_fluctuations(u_magnitudes, v_magnitudes, average_U_arr, average_V_arr)
print(Turbulent_kinetic_energy(Velocity_fluctuations_u, Velocity_fluctuations_v))"""
















