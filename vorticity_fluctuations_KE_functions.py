# imports
import numpy as np
import matplotlib.pyplot as plt
from positionfunction import position


def Vorticity(u_magnitudes, v_magnitudes, x_positions, y_positions):

    # Vorticity, defined as the curl of the velocity field

    # Input the 1D vector field in one of the planes, 
    # u_magnitudes (np.array(2 dimensions)), v_magnitudes (np.array(2 dimensions))
    # x_positions (np.array(1 dimension)), y_positions (np.array(1 dimension))
    # Output plots of the vorticity of the flow field

    # Change u_magnitudes and v_magnitudes to 2D arrays

    u_magnitudes, v_magnitudes = UandVmagnitudes1Dto2Dconverter(u_magnitudes, v_magnitudes)


    # Define the grid spacing
    dx = 0.9295 / 1000 # m
    dy = 0.9295 / 1000 # m

    # Calculate the partial derivatives of the velocity field, axis 1 is x, axis 0 is y
    dVx_dy = np.gradient(u_magnitudes, dy, axis=0)

    dVy_dx = np.gradient(v_magnitudes, dx, axis=1)
    
    # Calculate the vorticity field (it is a numpy array of the same shape as the input arrays)
    Vorticity_field = dVy_dx - dVx_dy
 
    # Create scatter plot
    plt.scatter(x_positions, y_positions, s=Vorticity_field, cmap='viridis') # 'c' is the colors, 'cmap' is the colormap

    # Adding a color bar to represent the magnitude of 'V'
    plt.colorbar(label='Magnitude of Vorticity Field')

    # Labelling the axes
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title('Scatter plot representing three variables')

    # Show plot
    plt.show()


# Mean flow velocity fluctuations, definded as the difference between the instantaneous velocity field and the mean velocity field

def Velocity_fluctuations(u_magnitudes, v_magnitudes, average_U_arr, average_V_arr,plane, J_number):
    # Check that both arrays are the same shape

    # Calculate the difference between the instantaneous velocity field and the mean velocity field
    Velocity_fluctuations_u = u_magnitudes - average_U_arr
    Velocity_fluctuations_v = v_magnitudes - average_V_arr

    #acquiring positions
    positions_file_path = f"{plane}_J{J_number}/XY.dat"
    positions = np.loadtxt(positions_file_path)  
    # Read data from files
    # Extract x, y positions from the positions data
    x_positions = positions[:, 0]
    y_positions = positions[:, 1]

    return Velocity_fluctuations_u, Velocity_fluctuations_v


# Turbulent kinetic energy, defined as the mean of the square of the velocity fluctuations

def Turbulent_kinetic_energy(Velocity_fluctuations_u, Velocity_fluctuations_v):
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
    
    
    #create zero-valued arrays with the same number of entries as u_magnitudes and v_magnitudes
    sum_v_squared = np.zeros(35738)
    sum_u_squared = np.zeros(35738)


    #for loop that for each bin, gets the velocity fluctuations, calculates the squares of the fluctuations, and adds them to a list
    for i in range(35):

        #add line that inputs u_magnitudes and v_magnitudes of current bin[i]
        #add line that gets the time averaged values: average_U_arr and average_V_arr


        #calculating velocity fluctuations
        Velocity_fluctuations_u, Velocity_fluctuations_v = Velocity_fluctuations(u_magnitudes, v_magnitudes, average_U_arr, average_V_arr)


        #calculating the squares of the values
        u_squared = np.square(Velocity_fluctuations_u)
        v_squared = np.square(Velocity_fluctuations_v)
    

        #adding the new values to the previous array
        sum_u_squared = np.add(sum_u_squared, u_squared)
        sum_v_squared = np.add(sum_v_squared, v_squared)


    #calculating mean of fluctuations squared
    mean_of_squares_u = sum_u_squared / 35
    mean_of_squares_v = sum_v_squared / 35
    
    turbulent_kinetic_energy = 0.5 * np.add(mean_of_squares_u, mean_of_squares_v)
    
    return turbulent_kinetic_energy

def UandVmagnitudes1Dto2Dconverter(u_magnitudes, v_magnitudes, plane, J_number):
    if plane == 'C':
        x_positions, y_positions = position(plane, J_number)

        # Determine grid dimensions based on grid_size
        n = len(np.unique(x_positions))
        m = len(np.unique(y_positions))

        # Initialize the 2D array to store velocity measurements
        u_magnitudes_2D, v_magnitudes_2D = np.zeros((n, m)), np.zeros((n, m))

        # Calculate the grid spacing based on the range of x and y positions
        x_min, x_max = np.min(x_positions), np.max(x_positions)
        y_min, y_max = np.min(y_positions), np.max(y_positions)

        x_step = (x_max - x_min) / (n - 1)
        y_step = (y_max - y_min) / (m - 1)

        # Map each velocity measurement to the corresponding grid position
        for x, y, vel in zip(x_positions, y_positions, u_magnitudes):
            # Calculate the grid indices for the given (x, y) position
            i = int((x - x_min) / x_step)
            j = int((y - y_min) / y_step)

            # Check if the indices are within the grid bounds
            if 0 <= i < n and 0 <= j < m:
                u_magnitudes_2D[i, j] = vel  # Assign velocity measurement to the grid

        for x, y, vel in zip(x_positions, y_positions, v_magnitudes):
            # Calculate the grid indices for the given (x, y) position
            i = int((x - x_min) / x_step)
            j = int((y - y_min) / y_step)

            # Check if the indices are within the grid bounds
            if 0 <= i < n and 0 <= j < m:
                v_magnitudes_2D[i, j] = vel  # Assign velocity measurement to the grid

    else:
        u_magnitudes_2D = np.array(u_magnitudes).reshape(167,214) # 167 rows, 214 columns
        v_magnitudes_2D = np.array(v_magnitudes).reshape(167,214)

    return u_magnitudes_2D, v_magnitudes_2D