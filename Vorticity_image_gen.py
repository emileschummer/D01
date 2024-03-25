import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import os
from matplotlib.cm import ScalarMappable


def Vorticity_image(u_magnitudes, v_magnitudes, plane, J_number):
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
    # 'c' is the colors, 'cmap' is the colormap

    # Adding a color bar to represent the magnitude of 'V'
    

    
    
     # Define colormap from dark blue to bright red
    cmap = plt.colormaps.get_cmap('gist_rainbow')

    # Normalize magnitudes to range from 0 to 1
    norm = Normalize(vmin=lowest_non_zero_magnitude, vmax=max_magnitude)

    # Set figure size and DPI for high-quality image
    fig, ax = plt.subplots(figsize=(12, 8), dpi=300)

    # Plotting Vector Field with QUIVER and colormap
    ax.scatter(x_positions, y_positions, s=Vorticity_field, cmap='viridis')
    ax.set_title('Vector Field with Color Scale')

    # Create a ScalarMappable object for colorbar
    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])  # Pass an empty array

    # Add colorbar using the ScalarMappable object
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Magnitude of Vorticity Field')
    
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_title('Scatter plot representing three variables')

    # Setting x, y boundary limits
    ax.set_xlim(np.min(x_positions) - 1, np.max(x_positions) + 1)
    ax.set_ylim(np.min(y_positions) - 1, np.max(y_positions) + 1)

    # Show plot with grid
    ax.grid()

    # Create directory for storing images if it doesn't exist
    output_directory = f"Results\{plane}\J{J_number}\Vorticity_fields"
    os.makedirs(output_directory, exist_ok=True)
    
    # Save the figure as a high-quality image in the output directory
    output_path = os.path.join(output_directory, f'bin_{bin}.png')
    plt.savefig(output_path, bbox_inches='tight')


    # Close the plot to release memory
    plt.close()

