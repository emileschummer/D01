import os
from vectorfieldtool import vectorfieldplot
import time
from vectorfieldmany import vectorfieldmany
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import Normalize
from matplotlib import cm
from matplotlib.cm import ScalarMappable
from interpolate import interpolpos
def average_vector_field(start_frame, end_frame, plane, J_number):
    
    data_directory = f"{plane}_J{J_number}/Velocity"
    frame_number = start_frame
    #amount of data points
    lenght_list = 35739
    
    #list of lists
    U_Velocities_lists=[]
    V_Velocities_lists=[]
    
    
    while True:
        # Construct the file path for the current frame
        file_path = os.path.join(data_directory, f"frame_{frame_number}.dat")
        
        #get velocities
        velocities = np.loadtxt(file_path)
        
        #create lists
        u_magnitudes = velocities[:, 0]
        v_magnitudes = velocities[:, 1]
        
        #append list of lists
        U_Velocities_lists.append(u_magnitudes)
        V_Velocities_lists.append(v_magnitudes)
        
        
        
        
        # Increment frame number
        frame_number += 1
        if frame_number>end_frame:
            break
        
        
        
        # Check if the next file exists
        next_file_path = os.path.join(data_directory, f"frame_{frame_number}.dat")
        if not os.path.exists(next_file_path):
            break  # Exit the loop if the next file doesn't exist
    
    
    #lenght of sublist        
    sublist_length = len(U_Velocities_lists[0])
    assert all(len(sublist) == sublist_length for sublist in U_Velocities_lists), "All sublists must have the same length"

    # Use a nested list comprehension to sum each sublist element-wise
    sum_U = [sum(sublist) for sublist in zip(*U_Velocities_lists)]

    
    #same method for V
    sublist_length = len(V_Velocities_lists[0])
    assert all(len(sublist) == sublist_length for sublist in V_Velocities_lists), "All sublists must have the same length"

    # Use a nested list comprehension to sum each sublist element-wise
    sum_V = [sum(sublist) for sublist in zip(*V_Velocities_lists)]
    
    #total amount of frames
    total_frames=end_frame-start_frame
    #U average
    # Divide each element in the sum_list by the divider
    average_U = [element / total_frames for element in sum_U]
    #V average
    # Divide each element in the sum_list by the divider
    average_V = [element / total_frames for element in sum_V]
    
    positions_file_path = f"{plane}_J{J_number}/XY.dat"
    positions = np.loadtxt(positions_file_path)  
    # Read data from files

    average_U_arr = np.array(average_U)
    average_V_arr = np.array(average_V)
    
    

    # Extract x, y positions from the positions data
    x_positions = positions[:, 0]
    y_positions = positions[:, 1]

    # Calculate magnitudes of each vector
    magnitudes = np.sqrt(average_U_arr * 2 + average_V_arr * 2)


    # Find the maximum magnitude
    max_magnitude = np.max(magnitudes)

    # Define colormap from dark blue to bright red
    cmap = plt.cm.get_cmap('gist_rainbow')

    # Normalize magnitudes to range from 0 to 1
    norm = Normalize(vmin=0, vmax=max_magnitude)

    # Plotting Vector Field with QUIVER and colormap
    plt.quiver(x_positions, y_positions, average_U_arr, average_V_arr, magnitudes, cmap=cmap, norm=norm)
    plt.title('Vector Field with Color Scale')

    # Add colorbar
    cbar = plt.colorbar()
    cbar.set_label('Magnitude')

    # Setting x, y boundary limits
    plt.xlim(np.min(x_positions) - 1, np.max(x_positions) + 1)
    plt.ylim(np.min(y_positions) - 1, np.max(y_positions) + 1)

    # Show plot with grid
    plt.grid()
    plt.show()  
def average_values(start_frame, end_frame, plane, J_number):
    # Define data directory
    data_directory = f"{plane}_J{J_number}/Velocity"
    
    # Initialize lists to store velocities
    U_Velocities_lists = []
    V_Velocities_lists = []
    
    # Loop through frames
    for frame_number in range(start_frame, end_frame + 1):
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
    
    return average_U, average_V    
def time_average_image(average_U_arr, average_V_arr, plane, J_number):
    positions_file_path = f"{plane}_J{J_number}/XY.dat"
    positions = np.loadtxt(positions_file_path)  

   
    
    
    
        
    x_positions = positions[:, 0]
    y_positions = positions[:, 1]    
        
    # Calculate magnitudes of each vector
    magnitudes = np.sqrt(average_U_arr * 2 + average_V_arr * 2)
    
    non_zero_magnitudes = magnitudes[magnitudes > 0]  # Filter out zero values
    lowest_non_zero_magnitude = np.min(non_zero_magnitudes)

    # scrub NaN values
    
    
    
        

    # Define colormap from dark blue to bright red
    cmap = plt.colormaps.get_cmap('magma')
    
    # Normalize magnitudes to range from 0 to 1
    norm = Normalize(vmin=lowest_non_zero_magnitude, vmax=np.percentile(magnitudes, 95))

    # Set figure size and DPI for high-quality image
    fig, ax = plt.subplots(figsize=(12, 8), dpi=300)

    # Plotting Vector Field with QUIVER and colormap
    ax.scatter(x_positions, y_positions,  c=magnitudes, cmap=cmap, norm=norm)
    ax.set_title('Vector Field with Color Scale')

    # Create a ScalarMappable object for colorbar
    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])  # Pass an empty array

    # Add colorbar using the ScalarMappable object
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Magnitude')

    # Setting x, y boundary limits
    ax.set_xlim(np.min(x_positions) - 1, np.max(x_positions) + 1)
    ax.set_ylim(np.min(y_positions) - 1, np.max(y_positions) + 1)

    # Show plot with grid
    ax.grid()
    
    if plane == 'C':
        # Load wall data points
        wall_file_path = f"C_J{J_number}/wall.dat"
        wall_data = np.loadtxt(wall_file_path)
        wall_x = wall_data[:, 0]
        wall_y = wall_data[:, 1]
        # Plot wall line
        ax.plot(wall_x, wall_y, color='blue', linestyle='-', linewidth=2, label='Wall')


    # Create directory for storing images if it doesn't exist
    output_directory = f"Zigzag_results/{plane}/Averaged_flow"
    os.makedirs(output_directory, exist_ok=True)
    
    # Save the figure as a high-quality image in the output directory
    output_path = os.path.join(output_directory, f'J_{J_number}.png')
    plt.savefig(output_path, bbox_inches='tight')


    # Close the plot to release memory
    plt.close()
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










output_dirr = 'fftplots'
os.makedirs(output_dirr, exist_ok=True)

average_U_arr, average_V_arr = average_values(1, 25, 'A', 0)#2500 frames
print('ok')
#time_average_image(average_U_arr, average_V_arr, 'A', 0)
velocities=np.column_stack((average_U_arr, average_V_arr))
positions_file_path = "A_J0/XY.dat"
positions = np.loadtxt(positions_file_path)
max_y = len(np.unique(positions[:, 1]))
max_x = len(np.unique(positions[:, 0]))
print(max_y,max_x)
matrix_shape = (max_y, max_x)
velocity_matrix = np.zeros(matrix_shape)
fill_matrix_from_bottom_left(velocity_matrix, np.linalg.norm(velocities, axis=1))
#print(velocity_matrix)

x_positions = positions[:, 0]
y_positions = positions[:, 1]  
ffttab = np.empty(max_x, dtype=object)
velocity_matrix = np.array(velocity_matrix)

graph_files= []

for i in range(max_x):
    if i == 0:
        continue  # Skip the first column (optional)

    if i % 50 == 0:
        print(i)
        #print("ve", len(freqs),freqs)

    # Select column, perform FFT, separate magnitude and phase
    #selected_column = velocity_matrix[:, i]
    ffttab = np.fft.rfft(velocity_matrix[:, i],n=84)#n=max_y=84
    magnitude = np.abs(ffttab)
    #phase = np.angle(ffttab[1:])
    sample_rate=100 
    freqs = np.fft.rfftfreq(n=84)
    magnitude=magnitude[1:]#remove first entry, since its 100 times higher than other values and its impossible to visualize it with one value being so large. I loo0ked into documentation I think the magnitude of the first entry of the output of the np.fft.rfft is an averaged magnitude of the flow, but im not sure of its physical meaning
    freqs = freqs[1:]
    plt.figure()
    plt.plot(freqs, magnitude, label=f'Column {i}')
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    plt.title(f'FFT Magnitude Spectrum for Column {i}')
    plt.xlim(0, 0.5)  # Set x-axis limits
    plt.ylim(0, 6)
    plt.legend()
    
    # Save the plot to the output directory
    plot_filename = os.path.join(output_dirr, f'fft_column_{i}.png')
    plt.savefig(plot_filename)
    plt.close()
    np.savetxt('ffttab.txt', ffttab, delimiter=',', fmt='%s')
    graph_files.append(plot_filename)
    plt.clf()

print(graph_files)
def update(frame):
    """
    Update function for the animation.

    Args:
    - frame: Frame index.
    """
    # Clear the current axis
    plt.cla()
    # Read the graph file for the current frame
    graph_file = graph_files[frame]
    # Display the graph
    img = plt.imread(graph_file)
    plt.imshow(img)
    plt.title(f"Frame {frame+1}/{len(graph_files)}")

# Directory containing the graphs
directory = 'fftplots'

# Read the graph files from the directory


# Create a matplotlib figure and axis
fig, ax = plt.subplots()

# Set up the animation
ani = FuncAnimation(fig, update, frames=len(graph_files), interval=200)

# Display the animation
plt.show()
