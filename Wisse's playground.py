from Bin_average_function import bin_average_vector_field
from Bin_average_function import Calc
from Bin_average_function import bin_average_velocities
from Vorticity_image_gen import Vorticity_image
from vorticity_fluctuations_KE_functions import Vorticity
from Bins import loadbin
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from positionfunction import position
plane='B'
bin=10
J_number=1

frames=loadbin(bin, plane, J_number)

average_U_arr, average_V_arr=Calc(frames, plane,J_number)

# List of lists
U_fluctuations_lists = []
V_fluctuations_lists = []
    
# Assuming you have defined data_directory and end_frame somewhere in your code
data_directory = f"{plane}_J{J_number}/Velocity"



for frame_number in frames:
        # Construct the file path for the current frame
        file_path = os.path.join(data_directory, f"frame_{frame_number}.dat")
        
        # Get velocities
        velocities = np.loadtxt(file_path)
        
        # Create lists
        u_magnitudes = velocities[:, 0]
        v_magnitudes = velocities[:, 1]
        
        
        #Calc fluctuations
        u_fluctuations=u_magnitudes-average_U_arr
        v_fluctuations=v_magnitudes-average_V_arr
        
        # Append list of lists
        U_fluctuations_lists.append(np.square(u_fluctuations))
        V_fluctuations_lists.append(np.square(v_magnitudes))

sublist_length = len(U_fluctuations_lists[0])
assert all(len(sublist) == sublist_length for sublist in U_fluctuations_lists), "All sublists must have the same length"

    # Use a nested list comprehension to sum each sublist element-wise
sum_U = [sum(sublist) for sublist in zip(*U_fluctuations_lists)]

    # Same method for V
sublist_length = len(V_fluctuations_lists[0])
assert all(len(sublist) == sublist_length for sublist in V_fluctuations_lists), "All sublists must have the same length"

    # Use a nested list comprehension to sum each sublist element-wise
sum_V = [sum(sublist) for sublist in zip(*V_fluctuations_lists)]
    
    # Total amount of frames
total_frames = len(frames)
    
    # U average
    # Divide each element in the sum_list by the divider
average_U = [element / total_frames for element in sum_U]
    
    # V average
    # Divide each element in the sum_list by the divider
average_V = [element / total_frames for element in sum_V]
    
    
    # np.array from files
average_U_arr = np.array(average_U)
average_V_arr = np.array(average_V)

turbulent_kinetic_energy = 0.5 * np.add(average_U, average_V)
x_positions, y_positions=position(plane, J_number)
    
plt.scatter(x_positions, y_positions, c=turbulent_kinetic_energy, cmap='gist_rainbow') # 'c' is the colors, 'cmap' is the colormap

# Adding a color bar to represent the magnitude of 'V'
plt.colorbar(label='Magnitude of Vorticity Field')

# Labelling the axes
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Scatter plot representing three variables')

# Show plot
plt.show()