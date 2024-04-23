import numpy as np
import os
for j in range(1,2501):
    positions_file_path = 'C_J0_unscrubbed\XY.dat'
    positions = np.loadtxt(positions_file_path)  

    velocity_file_path = f'C_J0_unscrubbed\Velocity/frame_{j}.dat'
    velocities = np.loadtxt(velocity_file_path)

    x_positions = positions[:, 0]
    y_positions = positions[:, 1]

    u_magnitudes = velocities[:, 0]
    v_magnitudes = velocities[:, 1]


    data = np.array([x_positions, y_positions, u_magnitudes, v_magnitudes]).T

    # Remove rows containing NaN values
    data = data[~np.isnan(data).any(axis=1)]

    # Separate X, Y, and magnitudes from the filtered data

    u_magnitudes_filtered = data[:, 2]
    v_magnitudes_filtered = data[:, 3]

    # Define the directory path and file path
    directory_V = "C_J0/Velocity"
    file_path_V = os.path.join(directory_V, f"frame_{j}.dat")

    # Create the directory if it doesn't exist
    if not os.path.exists(directory_V):
        os.makedirs(directory_V)

    # Save the filtered X and Y positions to the .dat file
    np.savetxt(file_path_V, np.column_stack((u_magnitudes_filtered, v_magnitudes_filtered)), fmt='%f', delimiter=' ', newline='\n')

# Define the directory path and file path
x_positions_filtered=data[:, 0]
y_positions_filtered=data[:, 1]
directory = "C_J0"
file_path= os.path.join(directory, "XY.dat")

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the filtered X and Y positions to the .dat file
np.savetxt(file_path, np.column_stack((x_positions_filtered, y_positions_filtered)), fmt='%f', delimiter=' ', newline='\n')

print("X and Y positions saved to", file_path_V)

'''for j in range(1,2501):
    velocity_file_path = f'C_J1_unscrubbed\Velocity/frame_{j}.dat'
    velocities = np.loadtxt(velocity_file_path)
    
    u_magnitudes = velocities[:, 0]
    v_magnitudes = velocities[:, 1]
    
    u_magnitudes = [u for i, u in enumerate(u_magnitudes) if i not in nan_indices]
    v_magnitudes = [v for i, v in enumerate(v_magnitudes) if i not in nan_indices]
    
    directory = "C_J1/Velocity"
    file_path = os.path.join(directory, f'frame_{j}.dat')
    
    
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write the X and Y positions to the .dat file
    with open(file_path, "w") as file:
        for x, y in zip(u_magnitudes, v_magnitudes):
            file.write(f"{x} {y}\n")'''

    
    
    