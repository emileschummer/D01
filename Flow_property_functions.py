# imports
import numpy as np

# Vorticity, defined as the curl of the velocity field
# Input the 2D vector field in one of the planes, output the vorticity field

def Vorticity(Velocity_field):

    # Claculate the partial derivatives of the velocity field
    dVx_dy = np.gradient(Velocity_field[0], axis=1)
    dVy_dx = np.gradient(Velocity_field[1], axis=0)

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

