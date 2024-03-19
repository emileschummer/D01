

"""

This is the main run file

"""

# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from averagefunction import average_values
from Bin_average_function import bin_average_velocities
from vorticity_fluctuations_KE_functions import Vorticity, Velocity_fluctuations, Turbulent_kinetic_energy

# Select the plane of interest and propeller configuration.


# Extract the data

    # Obtain unsteady flow field

    # Convert into time averaged flow fields
average_U_arr, average_V_arr = average_values(1, 4000)

    # Convert into bin averaged flow fields
u_magnitudes, v_magnitudes = bin_average_velocities(10)


# Obtain the flow properties for bin averaged flow fields and plot the flow properties / Visualize
Vorticity(u_magnitudes, v_magnitudes)
Velocity_fluctuations_u, Velocity_fluctuations_v = Velocity_fluctuations(u_magnitudes, v_magnitudes, average_U_arr, average_V_arr)
Turbulent_kinetic_energy(Velocity_fluctuations_u, Velocity_fluctuations_v)
















