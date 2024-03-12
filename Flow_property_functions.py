# imports
import numpy as np


"""

This works for 2D vector fields, in the x-y plane. 
The input is a 3D array, with the first two dimensions being the x and y coordinates, 
and the third dimension being the velocity components in the x and y directions (V_x and V_y).

"""


# Vorticity, defined as the curl of the velocity field
# Input the 2D vector field in one of the planes, output the vorticity field

def Vorticity(Velocity_field):

    # Claculate the partial derivatives of the velocity field, axis 1 is x, axis 0 is y
    dVx_dy = np.gradient(Velocity_field[:, :, 0], axis=0)
    dVy_dx = np.gradient(Velocity_field[:, :, 1], axis=1)

    # Calculate the vorticity field
    Vorticity_field = dVy_dx - dVx_dy

    return Vorticity_field


# Mean flow velocity fluctuations, definded as the difference between the instantaneous velocity field and the mean velocity field
# Input the instantaneous velocity field and the mean velocity field, output the velocity fluctuations field

def Velocity_fluctuations(Velocity_field, Average_velocity_field):

    # Check that both arrays are the same shape
    if Velocity_field.shape != Average_velocity_field.shape and isinstance(Average_velocity_field, np.ndarray) :
        print('Velocity_field and Average_velocity_field must be the same shape!')
    
    else:
         # Calculate the difference between the instantaneous velocity field and the mean velocity field
        Velocity_fluctuations = Velocity_field - Average_velocity_field

    return Velocity_fluctuations


# Turbulent kinetic energy, defined as the mean of the square of the velocity fluctuations
# Input the velocity fluctuations field, output the turbulent kinetic energy

def Turbulent_kinetic_energy(Velocity_fluctuations):

    # Calculate the square of the velocity fluctuations
    Velocity_fluctuations_squared_x = np.square(Velocity_fluctuations)[:, :, 0]
    Velocity_fluctuations_squared_y = np.square(Velocity_fluctuations)[:, :, 1]


    # Calculate the turbulent kinetic energy field  
    Turbulent_kinetic_energy_x = 0.5 * np.mean(Velocity_fluctuations_squared_x)
    Turbulent_kinetic_energy_y = 0.5 * np.mean(Velocity_fluctuations_squared_y)

    Turbulent_kinetic_energy = Turbulent_kinetic_energy_x + Turbulent_kinetic_energy_y
 
    return Turbulent_kinetic_energy


