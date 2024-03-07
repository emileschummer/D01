

def vectorfieldplot(file):
    #vector field expiriment
    import numpy as np 
    import matplotlib.pyplot as plt
    from matplotlib.colors import Normalize
    from matplotlib import cm
    


    positions_file_path = "Data/B_J1/XY.dat"
    positions = np.loadtxt(positions_file_path)  
    # Read data from files

    velocity_file_path = file
    velocities = np.loadtxt(velocity_file_path)
    # Assuming magnitudes_file.txt contains u, v magnitudes

    # Extract x, y positions from the positions data
    x_positions = positions[:, 0]
    y_positions = positions[:, 1]

    # Extract u, v magnitudes from the magnitudes data
    u_magnitudes = velocities[:, 0]
    v_magnitudes = velocities[:, 1]

    # Calculate magnitudes of each vector
    magnitudes = np.sqrt(u_magnitudes ** 2 + v_magnitudes ** 2)


    # Find the maximum magnitude
    max_magnitude = np.max(magnitudes)

    # Define colormap from dark blue to bright red
    cmap = plt.cm.get_cmap('coolwarm')

    # Normalize magnitudes to range from 0 to 1
    norm = Normalize(vmin=0, vmax=max_magnitude)

    # Plotting Vector Field with QUIVER and colormap
    plt.quiver(x_positions, y_positions, u_magnitudes, v_magnitudes, magnitudes, cmap=cmap, norm=norm)
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

import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import cm
import io
from datetime import datetime
import time

def vectorfieldpng(file, frame_number):
    positions_file_path = "Data/B_J1/XY.dat"
    positions = np.loadtxt(positions_file_path)  

    velocity_file_path = file
    velocities = np.loadtxt(velocity_file_path)

    x_positions = positions[:, 0]
    y_positions = positions[:, 1]

    u_magnitudes = velocities[:, 0]
    v_magnitudes = velocities[:, 1]

    magnitudes = np.sqrt(u_magnitudes ** 2 + v_magnitudes ** 2)
    max_magnitude = np.max(magnitudes)

    cmap = plt.colormaps.get_cmap('coolwarm')
    norm = Normalize(vmin=0, vmax=max_magnitude)

    fig, ax = plt.subplots()
    ax.quiver(x_positions, y_positions, u_magnitudes, v_magnitudes, magnitudes, cmap=cmap, norm=norm)
    ax.set_title('Vector Field with Color Scale')

    cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)
    cbar.set_label('Magnitude')

    ax.set_xlim(np.min(x_positions) - 1, np.max(x_positions) + 1)
    ax.set_ylim(np.min(y_positions) - 1, np.max(y_positions) + 1)

    ax.grid()

    # Save the plot as an image
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    save_path = f"C:\\Users\\Wisse de Vries\\Documents\\aerospace\\vectorfield_frame_{frame_number}.png"

    fig.savefig(save_path, format='png')
    plt.close(fig)  # Close the figure to release memory
    
    