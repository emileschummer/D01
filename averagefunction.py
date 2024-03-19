import os
from vectorfieldtool import vectorfieldplot
import time
from vectorfieldmany import vectorfieldmany
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import cm
# Define the directory containing the data files
data_directory = "B_J1/Velocity"


def average_vector_field(start_frame, end_frame):
    
    
    frame_number = start_frame
    #amount of data points
    lenght_list = 35739
    
    #list of lists
    U_Velocities_lists=[]
    V_Velocities_lists=[]
    
    
    while True:
        # Construct the file path for the current frame
        file_path = os.path.join(data_directory, f"frame_{frame_number}.dat")
        
        #get velocities
        velocities = np.loadtxt(file_path)
        
        #create lists
        u_magnitudes = velocities[:, 0]
        v_magnitudes = velocities[:, 1]
        
        #append list of lists
        U_Velocities_lists.append(u_magnitudes)
        V_Velocities_lists.append(v_magnitudes)
        
        
        
        
        # Increment frame number
        frame_number += 1
        if frame_number>end_frame:
            break
        
        
        
        # Check if the next file exists
        next_file_path = os.path.join(data_directory, f"frame_{frame_number}.dat")
        if not os.path.exists(next_file_path):
            break  # Exit the loop if the next file doesn't exist
    
    
    #lenght of sublist        
    sublist_length = len(U_Velocities_lists[0])
    assert all(len(sublist) == sublist_length for sublist in U_Velocities_lists), "All sublists must have the same length"

    # Use a nested list comprehension to sum each sublist element-wise
    sum_U = [sum(sublist) for sublist in zip(*U_Velocities_lists)]

    
    #same method for V
    sublist_length = len(V_Velocities_lists[0])
    assert all(len(sublist) == sublist_length for sublist in V_Velocities_lists), "All sublists must have the same length"

    # Use a nested list comprehension to sum each sublist element-wise
    sum_V = [sum(sublist) for sublist in zip(*V_Velocities_lists)]
    
    #total amount of frames
    total_frames=end_frame-start_frame
    #U average
    # Divide each element in the sum_list by the divider
    average_U = [element / total_frames for element in sum_U]
    #V average
    # Divide each element in the sum_list by the divider
    average_V = [element / total_frames for element in sum_V]
    
    positions_file_path = "B_J1/XY.dat"
    positions = np.loadtxt(positions_file_path)  
    # Read data from files

    average_U_arr = np.array(average_U)
    average_V_arr = np.array(average_V)
    
    

    # Extract x, y positions from the positions data
    x_positions = positions[:, 0]
    y_positions = positions[:, 1]

    # Calculate magnitudes of each vector
    magnitudes = np.sqrt(average_U_arr ** 2 + average_V_arr ** 2)


    # Find the maximum magnitude
    max_magnitude = np.max(magnitudes)

    # Define colormap from dark blue to bright red
    cmap = plt.cm.get_cmap('gist_rainbow')

    # Normalize magnitudes to range from 0 to 1
    norm = Normalize(vmin=0, vmax=max_magnitude)

    # Plotting Vector Field with QUIVER and colormap
    plt.quiver(x_positions, y_positions, average_U_arr, average_V_arr, magnitudes, cmap=cmap, norm=norm)
    plt.title('Vector Field with Color Scale')

    # Add colorbar
    cbar = plt.colorbar()
    cbar.set_label('Magnitude')

    # Setting x, y boundary limits
    plt.xlim(np.min(x_positions) - 1, np.max(x_positions) + 1)
    plt.ylim(np.min(y_positions) - 1, np.max(y_positions) + 1)

    # Show plot with grid
    plt.grid()
    plt.show()
    
def average_values(start_frame, end_frame):
        #define frame number
        frame_number=start_frame
        #amount of data points
        lenght_list = 35739
        
        #list of lists
        U_Velocities_lists=[]
        V_Velocities_lists=[]
        
        
        while True:
            # Construct the file path for the current frame
            file_path = os.path.join(data_directory, f"frame_{frame_number}.dat")
            
            #get velocities
            velocities = np.loadtxt(file_path)
            
            #create lists
            u_magnitudes = velocities[:, 0]
            v_magnitudes = velocities[:, 1]
            
            #append list of lists
            U_Velocities_lists.append(u_magnitudes)
            V_Velocities_lists.append(v_magnitudes)
            
            
            
            
            # Increment frame number
            frame_number += 1
            if frame_number>end_frame:
                break
            
            
            
            # Check if the next file exists
            next_file_path = os.path.join(data_directory, f"frame_{frame_number}.dat")
            if not os.path.exists(next_file_path):
                break  # Exit the loop if the next file doesn't exist
        
        
        #lenght of sublist        
        sublist_length = len(U_Velocities_lists[0])
        assert all(len(sublist) == sublist_length for sublist in U_Velocities_lists), "All sublists must have the same length"

        # Use a nested list comprehension to sum each sublist element-wise
        sum_U = [sum(sublist) for sublist in zip(*U_Velocities_lists)]

        
        #same method for V
        sublist_length = len(V_Velocities_lists[0])
        assert all(len(sublist) == sublist_length for sublist in V_Velocities_lists), "All sublists must have the same length"

        # Use a nested list comprehension to sum each sublist element-wise
        sum_V = [sum(sublist) for sublist in zip(*V_Velocities_lists)]
        
        #total amount of frames
        total_frames=end_frame-start_frame
        #U average
        # Divide each element in the sum_list by the divider
        average_U = [element / total_frames for element in sum_U]
        #V average
        # Divide each element in the sum_list by the divider
        average_V = [element / total_frames for element in sum_V]
        
        positions_file_path = "B_J1/XY.dat"
        positions = np.loadtxt(positions_file_path)  
        # Read data from files

        average_U_arr = np.array(average_U)
        average_V_arr = np.array(average_V)
        
        return average_U_arr, average_V_arr       