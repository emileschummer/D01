# imports
import numpy as np
import matplotlib.pyplot as plt


"""

This works for 2D vector fields, in the x-y plane. 
The input is a 3D array, with the first two dimensions being the x and y coordinates, 
and the third dimension being the velocity components in the x and y directions (V_x and V_y).

"""


# Vorticity, defined as the curl of the velocity field
# Input the 2D vector field in one of the planes, output the vorticity field

def Vorticity(u_magnitudes, v_magnitudes):
    print(u_magnitudes, v_magnitudes)
    #acquiring positions
    positions_file_path = "B_J1/XY.dat"
    positions = np.loadtxt(positions_file_path)  
    # Read data from files
    # Extract x, y positions from the positions data
    x_positions = positions[:, 0]
    print(x_positions)
    y_positions = positions[:, 1]
    print(y_positions)
    
    # Calculate the partial derivatives of the velocity field, axis 1 is x, axis 0 is y
    dVx_dy = np.gradient(u_magnitudes)
    print(dVx_dy)
    dVy_dx = np.gradient(v_magnitudes)
    
    #print(dVy_dx[1500])
    # Calculate the vorticity field
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
# Input the instantaneous velocity field and the mean velocity field, output the velocity fluctuations field

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
# Input the velocity fluctuations field, output the turbulent kinetic energy

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

def UandVmagnitudes1Dto2Dconverter(u_magnitudes, v_magnitudes):

    # TO USE THIS FUNCTION DO STH LIKE THIS: u_magnitudes, v_magnitudes (THIS ARE OLD, 1D LIST OF u and v magnitudes)= UandVmagnitudes1Dto2Dconverter(u_magnitudes, v_magnitudes)
    #the function returns 2D arrays of u_magnitudes and v_magnitudes 214 rows, 167 columns
    u_magnitudes_2D=np.array(u_magnitudes).reshape(214,167)
    v_magnitudes_2D=np.array(v_magnitudes).reshape(214,167)
    #array_2d = np.array(data).reshape(rows, cols)
    print(u_magnitudes_2D)
    return u_magnitudes_2D, v_magnitudes_2D