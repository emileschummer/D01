
import numpy as np

#function for posistion
def position(plane, J_number):
    #path to position file
    positions_file_path = f"{plane}_J{J_number}/XY.dat"
    #Np array of position
    positions = np.loadtxt(positions_file_path)
    #split X and Y coordinates  
    x_positions = positions[:, 0]
    y_positions = positions[:, 1]
    return x_positions, y_positions






