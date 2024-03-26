

"""

This is the main run file

"""

# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from averagefunction import average_values, time_average_image
from Bin_average_function import bin_average_velocities, bin_average_vector_field_image
from vorticity_fluctuations_KE_functions import Vorticity, Velocity_fluctuations, Turbulent_kinetic_energy
from Vorticity_image_gen import Vorticity_image, Velocity_fluctuations_image, Turbulent_kinetic_energy

# Select the plane of interest and propeller configuration.


# Extract the data

    # Obtain unsteady flow field

    # Convert into time averaged flow fields

    
average_U_arr, average_V_arr = average_values(1, 4000, 'B', 1)
time_average_image(average_U_arr, average_V_arr, 'B', 1)

    # Convert into bin averaged flow fields
for i in range(1, 37):
    u_magnitudes, v_magnitudes = bin_average_velocities(i, 'B', 1)
    if len(u_magnitudes)==0:
        break


# Obtain the flow properties for bin averaged flow fields and plot the flow properties / Visualize
    Vorticity_image(u_magnitudes, v_magnitudes, 'B', 1, i)
    # fluctuations_image
    Velocity_fluctuations_image(u_magnitudes, v_magnitudes, average_U_arr, average_V_arr, 'B', 1, i)
    # Turbulent kinetic energy
    Turbulent_kinetic_energy(u_magnitudes, v_magnitudes, average_U_arr, average_V_arr, 'B', 1, i)
    #vector fields
    bin_average_vector_field_image(i, 'B', 1)
    

















