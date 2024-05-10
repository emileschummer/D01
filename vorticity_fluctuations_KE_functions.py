import numpy as np
import matplotlib.pyplot as plt
from positionfunction import position


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


def Turbulent_kinetic_energy(Velocity_fluctuations_u, Velocity_fluctuations_v):
    
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


def UandVmagnitudes1Dto2Dconverter(u_magnitudes, v_magnitudes, x_positions, y_positions):

    # Determine grid dimensions based on grid_size
    x = np.unique(x_positions)
    y = np.unique(y_positions)
    n = len(x)
    m = len(y)

    # Create a 2D array for the u and v magnitudes
    u_magnitudes_2D = np.zeros((n, m))
    v_magnitudes_2D = np.zeros((n, m))

    # Fill the 2D arrays with the 1D data
    for i in range(len(u_magnitudes)):
        i_x = np.where(x == x_positions[i])[0]
        i_y = np.where(y == y_positions[i])[0]
        u_magnitudes_2D[i_x, i_y] = u_magnitudes[i]
        v_magnitudes_2D[i_x, i_y] = v_magnitudes[i]        

    return u_magnitudes_2D.T, v_magnitudes_2D.T
