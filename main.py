

"""

This is the main run file

"""

# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from averagefunction import average_values, time_average_image
from Bin_average_function import bin_average_velocities, bin_average_vector_field_image
from vorticity_fluctuations_KE_functions import Vorticity, Velocity_fluctuations
from Vorticity_image_gen import Vorticity_image, Velocity_fluctuations_image, Turbulent_kinetic_energy

# Select the plane of interest and propeller configuration.


# Extract the data

    # Obtain unsteady flow field

    # Convert into time averaged flow fields

Planes=['A', 'B']#Add C

for plane in Planes:
    print(plane)
    for j in range(1,2): #ADD 0
        average_U_arr, average_V_arr = average_values(1, 4000, plane, j)
        print('ok')
        time_average_image(average_U_arr, average_V_arr, plane, j)

            # Convert into bin averaged flow fields
        for i in range(1, 37):
            print('bin', i)
            error,u_magnitudes, v_magnitudes = bin_average_velocities(i, plane, j)
            if error==0:
                break


        # Obtain the flow properties for bin averaged flow fields and plot the flow properties / Visualize
            Vorticity_image(u_magnitudes, v_magnitudes, plane, j, i)
            # fluctuations_image
            Velocity_fluctuations_image(u_magnitudes, v_magnitudes, average_U_arr, average_V_arr, plane, j, i)
            # Turbulent kinetic energy
            Turbulent_kinetic_energy(u_magnitudes, v_magnitudes, average_U_arr, average_V_arr, plane, j, i)
            #vector fields
            bin_average_vector_field_image(i, plane, j)
    

















