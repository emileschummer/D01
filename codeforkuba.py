import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import os


def fill_matrix_from_bottom_left(matrix, values):
    m = len(matrix)
    n = len(matrix[0])
    
    # Start filling the matrix from the bottom left corner
    row = m - 1
    col = 0
    
    # Iterate through the values in reverse order and fill the matrix
    for value in reversed(values):
        matrix[row][col] = value
        col += 1
        if col == n:  # If reached the end of a row, move to the next row
            col = 0
            row -= 1
        if row < 0:  # Stop when reached the top row
            break

# Load position and velocity data
positions_file_path = "C_J0_unscrubbed/XY.dat"
positions = np.loadtxt(positions_file_path)


#load wall data
Wall_file_path = "C_J0/wall.dat"
Wall_positions= np.loadtxt(Wall_file_path)
#y wall pos
wall_plus_zero=np.column_stack((Wall_positions, np.zeros_like(Wall_positions[:,0])))


data_directory ="C_J0_unscrubbed\Velocity"

# Initialize lists to store velocities
U_Velocities_lists = []
V_Velocities_lists = []

# Loop through frames
for frame_number in range(1, 2500+1):
    # Construct file path for the current frame
    file_path = os.path.join(data_directory, f"frame_{frame_number}.dat")
   
    # Check if file exists
    if os.path.exists(file_path):
        # Load velocities from file
        velocities = np.loadtxt(file_path)
        
        # Extract U and V velocities
        u_magnitudes = velocities[:, 0]
        v_magnitudes = velocities[:, 1]
        
        # Append to velocity lists
        U_Velocities_lists.append(u_magnitudes)
        V_Velocities_lists.append(v_magnitudes)
       
    else:
        break  # Exit loop if file doesn't exist

# Calculate total frames
total_frames = len(U_Velocities_lists)

# Calculate average U and V velocities
average_U = np.sum(U_Velocities_lists, axis=0) / total_frames
average_V = np.sum(V_Velocities_lists, axis=0) / total_frames
velocities=np.column_stack((average_U, average_V))


# Determine the dimensions of the matrix based on unique values in position data
max_y = len(np.unique(positions[:, 1]))

# Create an empty matrix to store velocities
matrix_shape = ( max_y, 764)
velocity_matrix = np.zeros(matrix_shape)
position_matrix_x= np.zeros(matrix_shape)
position_matrix_y= np.zeros(matrix_shape)


# Fill the matrix from bottom left to top right with values from the list
fill_matrix_from_bottom_left(position_matrix_x, positions[:, 0])
fill_matrix_from_bottom_left(position_matrix_y, positions[:, 1])

fill_matrix_from_bottom_left(velocity_matrix, np.linalg.norm(velocities, axis=1))
print(matrix_shape)
# flip the filled matrix
velocity_matrix = velocity_matrix[:, ::-1]
position_matrix_x= position_matrix_x[:, ::-1]
position_matrix_y = position_matrix_y[:, ::-1]

number_of_interpolpoints=30
new_matrix_shape=(227+number_of_interpolpoints+1,764)
velocity_matrix_f = np.zeros(new_matrix_shape)
position_matrix_x_f= np.zeros(new_matrix_shape)
position_matrix_y_f= np.zeros(new_matrix_shape)

for i in range(0,763):
    #extract column
    column_index=i
    column_v= velocity_matrix[:, column_index]
    column_x= position_matrix_x[:, column_index]
    column_y= position_matrix_y[:, column_index]

    #combine the velocity column and position colum
    y_v_array=np.column_stack((column_x,column_y,column_v))

    # Boolean mask for identifying rows with NaN values
    nan_mask = np.isnan(y_v_array).any(axis=1)

    # Store the dropped rows in a separate array
    dropped_rows = y_v_array[nan_mask]

    # Clean the original array by removing rows with NaN values
    cleaned_array = y_v_array[~nan_mask]

    #last ten 
    last_ten_entries = cleaned_array[-15:]
    rest_entries = cleaned_array[:-15]

    #wall added to end of colum
    wall_added=np.vstack((last_ten_entries, wall_plus_zero[i]))
    
    #creates cubic spline
    
    spl=CubicSpline(-wall_added[:,1], wall_added[:,2])

    #top and bottum values and x value
    top_value = wall_added[-2, 1]
    bottom_value = wall_added[-1, 1]
    x_value=wall_added[0,0]
    #new positions
    new_positions=np.linspace(-top_value, -bottom_value, num=number_of_interpolpoints, endpoint=False)

    #new values
    new_values=spl(new_positions)
    new_x_pos=np.full(number_of_interpolpoints,x_value)

    #new array
    interpolated_val=np.column_stack((new_x_pos,-new_positions,new_values))

    #final col
    stack_1=np.insert(wall_added, -1, interpolated_val, axis=0)

    stack_2=np.vstack((rest_entries,stack_1))

    final_stack=np.vstack((stack_2,dropped_rows ))
    #replace
    
    position_matrix_x_f[:, i] = final_stack[:,0]
    position_matrix_y_f[:, i] = final_stack[:,1]
    velocity_matrix_f[:, i] = final_stack[:,2]



#boundary layer plot bottom 25+new points
position_matrix_xb=position_matrix_x_f[-25-number_of_interpolpoints:]
position_matrix_yb=position_matrix_y_f[-25-number_of_interpolpoints:]
velocity_matrix_b=velocity_matrix_f[-25-number_of_interpolpoints:]


x_flat = position_matrix_x_f.flatten()
y_flat = position_matrix_y_f.flatten()
velocities_flat = velocity_matrix_f.flatten()


norm = plt.Normalize(0, 10)

wall_file_path = f"C_J{0}_unscrubbed/wall.dat"
wall_data = np.loadtxt(wall_file_path)
wall_x = wall_data[:, 0]
wall_y = wall_data[:, 1]
# Plot wall line
plt.plot(wall_x, wall_y, color='red', linestyle='-', linewidth=0, label='Wall')

plt.scatter(x_flat, y_flat, s=1, c=velocities_flat, cmap='tab20b', norm=norm)
plt.colorbar(label='Velocity')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Scatter Plot of Positions with Velocities')
plt.grid(True)
plt.show()