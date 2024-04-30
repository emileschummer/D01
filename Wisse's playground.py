from collections import defaultdict
import numpy as np


#path to position file
positions_file_path = f"{'C'}_J{0}/XY.dat"
#Np array of position
positions = np.loadtxt(positions_file_path)




def find_lowest_y(points):
    # Create a defaultdict to store points by their x coordinate
    points_by_x = defaultdict(list)
    
    # Populate the defaultdict and keep track of indices
    indices_by_y = defaultdict(list)
    for index, (x, y) in enumerate(points):
        points_by_x[x].append(y)
        indices_by_y[y].append(index)
    
    # Create a dictionary to store the lowest y value for every x position
    lowest_y_by_x = {}
    
    # Create a list to store indices of lowest y values
    lowest_y_indices = []
    
    # Iterate over each x position
    for x, y_values in points_by_x.items():
        # Find the minimum y value for the current x position
        lowest_y = min(y_values)
        # Store the lowest y value for the current x position
        lowest_y_by_x[x] = lowest_y
        # Get indices of the lowest y value(s) and add to the list
        lowest_y_indices.extend(indices_by_y[lowest_y])
    
    return lowest_y_by_x

# Example usage:

lowest_y_by_x = find_lowest_y(positions)
print(len(lowest_y_by_x), 'number of points')


velocity_file_path = 'C_J0\Velocity/frame_1.dat'
velocities = np.loadtxt(velocity_file_path)
    

# Extract u, v magnitudes from the magnitudes data
u_magnitudes = velocities[:, 0]
v_magnitudes = velocities[:, 1]



'''print("Lowest y value for every x position:")
for x, lowest_y in lowest_y_by_x.items():
    print(f"x = {x}, lowest y = {lowest_y}")'''
    
lowest_y_array = np.array(list(lowest_y_by_x.items()))    
print(lowest_y_array)
step_size=0.2559

wall_file_path = f"{'C'}_J{0}/wall.dat"
#Np array of position
wall_positions = np.loadtxt(wall_file_path)
wall_postion_y=wall_positions[:, 1]


#spacing array
space_array=lowest_y_array-wall_positions
space_array=space_array[:, 1]
#amount of steps
amount_of_steps=space_array/step_size

rounded_steps=np.floor(amount_of_steps)






'''
duplicate_pairs = []

# Iterate over each row
for i, row1 in enumerate(wall_positions):
    # Iterate over subsequent rows
    for j, row2 in enumerate(wall_positions[i+1:], start=i+1):
        # Check if the current pair of rows are identical
        if np.array_equal(row1, row2):
            # If identical, append the pair to the list of duplicate pairs
            duplicate_pairs.append((i, j))

print("Duplicate pairs:")
print(duplicate_pairs)
'''





# Find unique x values
unique_xs = np.unique(positions[:, 0])

# Initialize an array to hold the results
min_indices = []

# Find the index of the minimum y for each x
for x in unique_xs:
    # Filter rows where the x value matches
    filtered_rows = positions[positions[:, 0] == x]
    
    # Find the index of the minimum y in the filtered rows
    min_y_index = np.argmin(filtered_rows[:, 1])
    
    # Convert to original index in the full data array
    # This step involves finding the original row index of the filtered minimum y index
    original_index = np.where(positions[:, 0] == x)[0][min_y_index]
    
    # Store the x value and its corresponding index of minimum y
    min_indices.append((x, original_index))


    
extracted_u = [u_magnitudes[i[1]] for i in min_indices]
print(len(extracted_u))

extracted_v = [v_magnitudes[i[1]] for i in min_indices]
    
Mu_array=np.divide(extracted_u,space_array)

Mv_array=np.divide(extracted_v,space_array)

Cu=-Mu_array*wall_postion_y
Cv=-Mv_array*wall_postion_y



# Initialize a list to store new y values and corresponding x values
new_ys = []
expanded_xs = []

# Generate new y values and repeat x values accordingly
for x, y, n in zip(xs, ys, ns):
    # Create an array of n new y values starting from y, with step_size increments
    new_y_values = y + np.arange(1, n + 1) * step_size
    new_ys.append(new_y_values)
    
    # Repeat x value n times
    repeated_xs = np.full(n, x)
    expanded_xs.append(repeated_xs)

# Convert list of arrays into a single array for easier handling
new_ys_array = np.concatenate(new_ys)
expanded_xs_array = np.concatenate(expanded_xs)

# Combine x and y values into a single array
missing_positions = np.column_stack((expanded_xs_array, new_ys_array))

#calculate u and v values for missing positions
missing_v = (Mv_array * missing_positions[:, 1]) + Cv
missing_u = (Mu_array * missing_positions[:, 1]) + Cu

