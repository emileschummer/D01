import numpy as np
from collections import defaultdict

def interpol(u,v):
    '''#path to position file
    positions_file_path = f"{'C'}_J{0}/XY.dat"
    #Np array of position
    positions = np.loadtxt(positions_file_path)

    xs=positions[:763, 0]


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
    u_magnitudes = u
    v_magnitudes = v



    print("Lowest y value for every x position:")
    for x, lowest_y in lowest_y_by_x.items():
        print(f"x = {x}, lowest y = {lowest_y}")
        
    lowest_y_array = np.array(list(lowest_y_by_x.items()))    

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
    rounded_steps=rounded_steps.astype(int)





    
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


    extracted_v = [v_magnitudes[i[1]] for i in min_indices]
        
    Mu_array=np.divide(extracted_u,space_array)

    Mv_array=np.divide(extracted_v,space_array)

    Cu=-Mu_array*wall_postion_y
    Cv=-Mv_array*wall_postion_y


    # Initialize a list to store new y values and corresponding x values
    new_ys = []
    expanded_xs = []

    # Generate new y values and repeat x values accordingly
    for x, y, n in zip(lowest_y_array[:,0], lowest_y_array[:,1], rounded_steps):
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
    missing_v=[]
    missing_u=[]
    j=0
    print(len(missing_positions[:,0]))
    for i in range(len(missing_positions[:,0])):  
        
        xi = missing_positions[i, 0]
        
        if i != 0:
            ximinusone =  missing_positions[i-1, 0]
        else: 
            ximinusone = xi
        
        if xi == ximinusone:
            missing_v.append( (Mv_array[j] * missing_positions[i, 1]) + Cv[j])
            missing_u.append( (Mu_array[j] * missing_positions[i, 1]) + Cu[j])
            
        else: 
            j=j+1
            
            missing_v.append( (Mv_array[j] * missing_positions[i, 1]) + Cv[j])
            missing_u.append( (Mu_array[j] * missing_positions[i, 1]) + Cu[j])
    print(missing_v.shape)
    complete_v=np.hstack((v_magnitudes, missing_v))
    complete_u=np.hstack((u_magnitudes, missing_u))
    
    print(len(complete_v), 'pizza')
    print(complete_u)
    
    return complete_u, complete_v'''
    import numpy as np
    from scipy.interpolate import griddata
    import os
    import matplotlib.pyplot as plt
    from matplotlib.colors import Normalize
    from matplotlib import cm

    import numpy as np
    from scipy.interpolate import griddata
    positions_file_path = f"{'C'}_J{0}/XY.dat"
    positions = np.loadtxt(positions_file_path)
    
    wall_file_path = f"{'C'}_J{0}/wall.dat"
    #Nparray of position
    wall_positions = np.loadtxt(wall_file_path)

    # Sample data: replace these with your actual data arrays
    existing_points = np.array(positions)  # Existing (x, y) points
    existing_u = np.array(u)                  # u components at existing points
    existing_v = np.array(v)                  # v components at existing points
    wall_points = np.array(wall_positions)  # Airfoil wall (x, y) points

    # Function to generate intermediate points
    def generate_intermediate_points(existing_points, wall_points, num_points=5):
        # Linearly interpolate between existing points and wall points
        all_inter_points = []
        for ep, wp in zip(existing_points, wall_points):
            for t in np.linspace(0, 1, num_points + 2)[1:-1]:
                inter_point = ep * (1 - t) + wp * t
                all_inter_points.append(inter_point)
        return np.array(all_inter_points)

    # Generate new points
    new_points = generate_intermediate_points(existing_points, wall_points)

    # Combine all points for interpolation
    all_points = np.vstack([existing_points, wall_points])
    all_u = np.concatenate([existing_u, np.zeros(len(wall_points))])
    all_v = np.concatenate([existing_v, np.zeros(len(wall_points))])

    # Interpolation function using griddata
    def interpolate_velocities(points, values, new_points):
        return griddata(points, values, new_points, method='linear')

    # Interpolate u and v components
    new_u = interpolate_velocities(all_points, all_u, new_points)
    new_v = interpolate_velocities(all_points, all_v, new_points)
    # Example of handling NaNs by setting them to zero or another appropriate value
    new_u = np.nan_to_num(new_u, nan=0)
    new_v = np.nan_to_num(new_v, nan=0)

    total_pos=np.vstack((positions, new_points))
    total_u=np.hstack((u,new_u))
    # Output new positions and their corresponding velocities
    print("New Points:", new_points)
    print("Interpolated U:", new_u)
    print("Interpolated V:", new_v)

    # Define colormap from dark blue to bright red
    cmap = plt.cm.get_cmap('bwr')

    # Normalize magnitudes to range from 0 to 1
    norm = Normalize(vmin=0, vmax=10)

    # Plotting Vector Field with QUIVER and colormap
    plt.scatter(total_pos[:,0],total_pos[:,1], c=total_u, cmap=cmap, norm=norm)
    plt.title('Vector Field with Color Scale')
    # Load wall data points
    wall_file_path = f"C_J{0}/wall.dat"
    wall_data = np.loadtxt(wall_file_path)
    wall_x = wall_data[:, 0]
    wall_y = wall_data[:, 1]
    # Plot wall line
    plt.plot(wall_x, wall_y, color='blue', linestyle='-', linewidth=2, label='Wall')


    # Add colorbar
    cbar = plt.colorbar()
    cbar.set_label('magnitude')

    # Setting x, y boundary limits
    plt.xlim(np.min(total_pos[:,0]) - 1, np.max(total_pos[:,0]) + 1)
    plt.ylim(np.min(total_pos[:,1]) - 1, np.max(total_pos[:,1]) + 1)

    # Show plot with grid
    plt.grid()
    plt.show()


    '''
    positions_file_path = f"{'C'}_J{0}/XY.dat"
    positions = np.loadtxt(positions_file_path)

    x_positions = positions[:, 0]
    y_positions = positions[:, 1]

    data_directory = f"{'C'}_J{0}/Velocity"
        
        

    # Construct the file path for the current frame
    file_path = os.path.join(data_directory, f"frame_{1}.dat")

    # Get velocities
    velocities = np.loadtxt(file_path)

    # Create lists
    u_components = u
    v_components = v

    wall_file_path = f"{'C'}_J{0}/wall.dat"
    #Np array of position
    wall_positions = np.loadtxt(wall_file_path)
    y_wall=wall_positions[:, 1] 
    x_wall=wall_positions[:, 0] 



    x = np.array(x_positions)
    y = np.array(y_positions)
    u = np.array(u_components)
    v = np.array(v_components)

    x_wall = np.array(x_wall)
    y_wall = np.array(y_wall)



    # Create a dense grid
    grid_x, grid_y = np.meshgrid(
        np.linspace(min(x.min(), x_wall.min()), max(x.max(), x_wall.max()), 764),
        np.linspace(min(y.min(), y_wall.min()), max(y.max(), y_wall.max()), 218)
    )


    # Append the wall data with zero velocities
    x_full = np.append(x, x_wall)
    y_full = np.append(y, y_wall)
    u_full = np.append(u, np.zeros_like(x_wall))
    v_full = np.append(v, np.zeros_like(y_wall))

    # Interpolate using griddata
    u_interp = griddata((x_full, y_full), u_full, (grid_x, grid_y), method='cubic')
    v_interp = griddata((x_full, y_full), v_full, (grid_x, grid_y), method='cubic')


    u_interp = np.nan_to_num(u_interp, nan=np.nanmean(u_interp))
    v_interp = np.nan_to_num(v_interp, nan=np.nanmean(v_interp))
    print(u_interp)

    # Define colormap from dark blue to bright red
    cmap = plt.cm.get_cmap('bwr')

    # Normalize magnitudes to range from 0 to 1
    norm = Normalize(vmin=0, vmax=10)

    # Plotting Vector Field with QUIVER and colormap
    plt.scatter(grid_x,grid_y, c=u_interp, cmap=cmap, norm=norm)
    plt.title('Vector Field with Color Scale')


    # Add colorbar
    cbar = plt.colorbar()
    cbar.set_label('magnitude')

    # Setting x, y boundary limits
    plt.xlim(np.min(x_positions) - 1, np.max(x_positions) + 1)
    plt.ylim(np.min(y_positions) - 1, np.max(y_positions) + 1)

    # Show plot with grid
    plt.grid()
    plt.show()
    return u_interp, v_interp
    '''
    
    



def interpolpos(positions):
    xs=positions[:763, 0]


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
        

    



    '''print("Lowest y value for every x position:")
    for x, lowest_y in lowest_y_by_x.items():
        print(f"x = {x}, lowest y = {lowest_y}")'''
        
    lowest_y_array = np.array(list(lowest_y_by_x.items()))    

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
    rounded_steps=rounded_steps.astype(int)





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


        
    


    # Initialize a list to store new y values and corresponding x values
    new_ys = []
    expanded_xs = []

    # Generate new y values and repeat x values accordingly
    for x, y, n in zip(lowest_y_array[:,0], lowest_y_array[:,1], rounded_steps):
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
    complete_p=np.vstack((positions, missing_positions))
    print(len(complete_p), 'ananas')
    return complete_p
    