import os
from vectorfieldtool import vectorfieldplot

from vectorfieldmany import vectorfieldmany
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import cm
from Bins import loadbin
# Define the directory containing the data files
data_directory = "Data/B_J1/Velocity"






def bin_average_vector_field(bin):
    
    
    frames=loadbin(bin)
    
    
    #amount of data points
    lenght_list = 35739
    
    #list of lists
    U_Velocities_lists=[]
    V_Velocities_lists=[]
    print(frames)
    
    for frame_number in frames:
        # Construct the file path for the current frame
        file_path = os.path.join(data_directory, f"frame_{frame_number}.dat")
        print(frame_number)
        # Get velocities
        velocities = np.loadtxt(file_path)
        
        # Create lists
        u_magnitudes = velocities[:, 0]
        v_magnitudes = velocities[:, 1]
        
        # Append list of lists
        U_Velocities_lists.append(u_magnitudes)
        V_Velocities_lists.append(v_magnitudes)
        
    
    
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
    total_frames=len(frames)
    #U average
    # Divide each element in the sum_list by the divider
    average_U = [element / total_frames for element in sum_U]
    #V average
    # Divide each element in the sum_list by the divider
    average_V = [element / total_frames for element in sum_V]
    
    positions_file_path = "Data/B_J1/XY.dat"
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
    


def bin_average_vector_field_image(bin):
    frames = loadbin(bin)
    
    # Amount of data points
    length_list = 35739
    
    # List of lists
    U_Velocities_lists = []
    V_Velocities_lists = []
    
    # Assuming you have defined data_directory and end_frame somewhere in your code
    data_directory = 'path_to_data_directory'
    end_frame = 100  # Example end_frame
    
    for frame_number in frames:
        # Construct the file path for the current frame
        file_path = os.path.join(data_directory, f"frame_{frame_number}.dat")
        
        # Get velocities
        velocities = np.loadtxt(file_path)
        
        # Create lists
        u_magnitudes = velocities[:, 0]
        v_magnitudes = velocities[:, 1]
        
        # Append list of lists
        U_Velocities_lists.append(u_magnitudes)
        V_Velocities_lists.append(v_magnitudes)
        
    # Length of sublist        
    sublist_length = len(U_Velocities_lists[0])
    assert all(len(sublist) == sublist_length for sublist in U_Velocities_lists), "All sublists must have the same length"

    # Use a nested list comprehension to sum each sublist element-wise
    sum_U = [sum(sublist) for sublist in zip(*U_Velocities_lists)]

    # Same method for V
    sublist_length = len(V_Velocities_lists[0])
    assert all(len(sublist) == sublist_length for sublist in V_Velocities_lists), "All sublists must have the same length"

    # Use a nested list comprehension to sum each sublist element-wise
    sum_V = [sum(sublist) for sublist in zip(*V_Velocities_lists)]
    
    # Total amount of frames
    total_frames = len(frames)
    
    # U average
    # Divide each element in the sum_list by the divider
    average_U = [element / total_frames for element in sum_U]
    
    # V average
    # Divide each element in the sum_list by the divider
    average_V = [element / total_frames for element in sum_V]
    
    positions_file_path = "Data/B_J1/XY.dat"
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

    # Set figure size and DPI for high-quality image
    fig, ax = plt.subplots(figsize=(12, 8), dpi=300)

    # Plotting Vector Field with QUIVER and colormap
    ax.quiver(x_positions, y_positions, average_U_arr, average_V_arr, magnitudes, cmap=cmap, norm=norm)
    ax.set_title('Vector Field with Color Scale')

    # Add colorbar
    cbar = plt.colorbar(ax=ax)
    cbar.set_label('Magnitude')

    # Setting x, y boundary limits
    ax.set_xlim(np.min(x_positions) - 1, np.max(x_positions) + 1)
    ax.set_ylim(np.min(y_positions) - 1, np.max(y_positions) + 1)

    # Show plot with grid
    ax.grid()

    # Create directory if it doesn't exist
    bin_directory = 'Bin_vector_field'
    os.makedirs(bin_directory, exist_ok=True)
    
    # Save the figure as a high-quality image in the bin directory
    output_path = os.path.join(bin_directory, f'bin_{bin}_vector_field.png')
    plt.savefig(output_path, bbox_inches='tight')

    # Close the plot to release memory
    plt.close()

    # Return the output path
    return output_path