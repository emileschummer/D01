import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import os
from matplotlib.cm import ScalarMappable
from vorticity_fluctuations_KE_functions import Velocity_fluctuations
from positionfunction import position
from Bins import loadbin
from Bin_average_function import Calc


def Vorticity_image(u_magnitudes, v_magnitudes, plane, J_number, bin):
    
    
    #load positions
    x_positions, y_positions=position(plane, J_number)
    
    
    # Calculate the partial derivatives of the velocity field, axis 1 is x, axis 0 is y
    dVx_dy = np.gradient(u_magnitudes)
    
    dVy_dx = np.gradient(v_magnitudes)
    
    #print(dVy_dx[1500])
    # Calculate the vorticity field
    Vorticity_field = dVy_dx - dVx_dy

    # Create scatter plot
    # 'c' is the colors, 'cmap' is the colormap

    # Adding a color bar to represent the magnitude of 'V'
    

    
    
    # Define colormap from dark blue to bright red
    cmap = plt.colormaps.get_cmap('bwr')

    # Normalize magnitudes to range from 0 to 1
    norm = Normalize(vmin=-0.5, vmax=0.5)

    # Set figure size and DPI for high-quality image
    fig, ax = plt.subplots(figsize=(12, 8), dpi=300)

    # Plotting Vector Field with QUIVER and colormap
    ax.scatter(x_positions, y_positions, s=Vorticity_field, c=Vorticity_field, cmap=cmap, norm=norm)
    ax.set_title('Vector Field with Color Scale')

    # Create a ScalarMappable object for colormap
    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])  # Pass an empty array

    # Add colorbar using the ScalarMappable object
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Magnitude of Vorticity Field')
    
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_title('Vorticity field')

    # Setting x, y boundary limits
    ax.set_xlim(np.min(x_positions) - 1, np.max(x_positions) + 1)
    ax.set_ylim(np.min(y_positions) - 1, np.max(y_positions) + 1)

    # Show plot with grid
    ax.grid()

    # Create directory for storing images if it doesn't exist
    output_directory = f"Results\{plane}\J{J_number}\Vorticity_fields"
    os.makedirs(output_directory, exist_ok=True)
    
    # Save the figure as a high-quality image in the output directory
    output_path = os.path.join(output_directory, f'bin_{bin}.png')
    plt.savefig(output_path, bbox_inches='tight')


    # Close the plot to release memory
    plt.close()



def Velocity_fluctuations_image(u_magnitudes, v_magnitudes, average_U_arr, average_V_arr, plane, J_number, bin):
    # Check that both arrays are the same shape

    # Calculate the difference between the instantaneous velocity field and the mean velocity field
    Velocity_fluctuations_u = u_magnitudes - average_U_arr
    Velocity_fluctuations_v = v_magnitudes - average_V_arr

    x_positions, y_positions=position(plane, J_number)
    # Define colormap from dark blue to bright red
    cmap = plt.colormaps.get_cmap('gist_rainbow')

    # Normalize magnitudes to range from 0 to 1
    norm = Normalize(vmin=np.min(Velocity_fluctuations_u), vmax=np.max(Velocity_fluctuations_u))

    
    
    # Set figure size and DPI for high-quality image
    fig, ax = plt.subplots(figsize=(12, 8), dpi=300)

    # Plotting Vector Field with QUIVER and colormap
    ax.scatter(x_positions, y_positions, c=Velocity_fluctuations_u, cmap=cmap, norm=norm)
    ax.set_title('Vector Field with Color Scale')

    # Create a ScalarMappable object for colormap
    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])  # Pass an empty array

    # Add colorbar using the ScalarMappable object
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Magnitude of velocity fluctations U')
    
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_title('Scatter plot U fluctations')

    # Setting x, y boundary limits
    ax.set_xlim(np.min(x_positions) - 1, np.max(x_positions) + 1)
    ax.set_ylim(np.min(y_positions) - 1, np.max(y_positions) + 1)

    # Show plot with grid
    ax.grid()

    # Create directory for storing images if it doesn't exist
    output_directory = f"Results\{plane}\J{J_number}\Fluctations_fields"
    os.makedirs(output_directory, exist_ok=True)
    
    # Save the figure as a high-quality image in the output directory
    output_path = os.path.join(output_directory, f'bin_{bin}_U.png')
    plt.savefig(output_path, bbox_inches='tight')


    # Close the plot to release memory
    plt.close()
        # Set figure size and DPI for high-quality image
    fig, ax = plt.subplots(figsize=(12, 8), dpi=300)
    norm = Normalize(vmin=np.min(Velocity_fluctuations_v), vmax=np.max(Velocity_fluctuations_v))
    # Plotting Vector Field with QUIVER and colormap
    ax.scatter(x_positions, y_positions, c=Velocity_fluctuations_v, cmap=cmap, norm=norm)
    ax.set_title('Vector Field with Color Scale')

    # Create a ScalarMappable object for colormap
    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])  # Pass an empty array

    # Add colorbar using the ScalarMappable object
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Magnitude of velocity fluctations V')
    
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_title('Scatter plot V fluctations')

    # Setting x, y boundary limits
    ax.set_xlim(np.min(x_positions) - 1, np.max(x_positions) + 1)
    ax.set_ylim(np.min(y_positions) - 1, np.max(y_positions) + 1)

    # Show plot with grid
    ax.grid()

    # Create directory for storing images if it doesn't exist
    output_directory = f"Results\{plane}\J{J_number}\Fluctations_fields"
    os.makedirs(output_directory, exist_ok=True)
    
    # Save the figure as a high-quality image in the output directory
    output_path = os.path.join(output_directory, f'bin_{bin}_V.png')
    plt.savefig(output_path, bbox_inches='tight')


    # Close the plot to release memory
    plt.close()
    
    
def Turbulent_kinetic_energy(plane, J_number, bin):
    """
    # Calculate the square of the velocity fluctuations
    Velocity_fluctuations_squared_u = np.square(Velocity_fluctuations_u)
    Velocity_fluctuations_squared_v = np.square(Velocity_fluctuations_v)

    # Calculate the turbulent kinetic energy field x and y
    Turbulent_kinetic_energy_u = 0.5 * np.mean(Velocity_fluctuations_squared_u)
    Turbulent_kinetic_energy_v = 0.5 * np.mean(Velocity_fluctuations_squared_v)

    # Combine both to get the total turbulent kinetic energy

    Turbulent_kinetic_energy = Turbulent_kinetic_energy_u + Turbulent_kinetic_energy_v
    """
    
    
    """#create zero-valued arrays with the same number of entries as u_magnitudes and v_magnitudes
    sum_v_squared = np.zeros(35738)
    sum_u_squared = np.zeros(35738)


    #for loop that for each bin, gets the velocity fluctuations, calculates the squares of the fluctuations, and adds them to a list
    

        #add line that inputs u_magnitudes and v_magnitudes of current bin[i]
        #add line that gets the time averaged values: average_U_arr and average_V_arr


        #calculating velocity fluctuations
    Velocity_fluctuations_u, Velocity_fluctuations_v = Velocity_fluctuations(u_magnitudes, v_magnitudes, average_U_arr, average_V_arr, plane, J_number)


        #calculating the squares of the values
    u_squared = np.square(Velocity_fluctuations_u)
    v_squared = np.square(Velocity_fluctuations_v)
    

        #adding the new values to the previous array
    sum_u_squared = np.add(sum_u_squared, u_squared)
    sum_v_squared = np.add(sum_v_squared, v_squared)


    #calculating mean of fluctuations squared
    mean_of_squares_u = sum_u_squared / 35
    mean_of_squares_v = sum_v_squared / 35
    
    turbulent_kinetic_energy = 0.5 * np.add(mean_of_squares_u, mean_of_squares_v)"""
    
    
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
            V_fluctuations_lists.append(np.square(v_fluctuations))

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
    
    
    
        # Define colormap from dark blue to bright red
    cmap = plt.colormaps.get_cmap('gist_rainbow')

    # Normalize magnitudes to range from 0 to 1
    norm = Normalize(vmin=0, vmax=np.max(turbulent_kinetic_energy))
    
    
    fig, ax = plt.subplots(figsize=(12, 8), dpi=300)

    # Plotting Vector Field with QUIVER and colormap
    ax.scatter(x_positions, y_positions, c=turbulent_kinetic_energy, cmap=cmap, norm=norm)
    ax.set_title('Turbulent kinetic energy field')

    # Create a ScalarMappable object for colormap
    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])  # Pass an empty array

    # Add colorbar using the ScalarMappable object
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Magnitude of Turbulent kinetic energy')
    
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_title('Scatter plot Turbulent kinetic energy')

    # Setting x, y boundary limits
    ax.set_xlim(np.min(x_positions) - 1, np.max(x_positions) + 1)
    ax.set_ylim(np.min(y_positions) - 1, np.max(y_positions) + 1)

    # Show plot with grid
    ax.grid()

    # Create directory for storing images if it doesn't exist
    output_directory = f"Results\{plane}\J{J_number}\Turbelentkineticenergy_fields"
    os.makedirs(output_directory, exist_ok=True)
    
    # Save the figure as a high-quality image in the output directory
    output_path = os.path.join(output_directory, f'bin_{bin}.png')
    plt.savefig(output_path, bbox_inches='tight')


    # Close the plot to release memory
    plt.close()