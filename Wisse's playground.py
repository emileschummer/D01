
#vector field expiriment
import numpy as np 
import matplotlib.pyplot as plt



positions_file_path = "Data/B_J1/XY.dat"
positions = np.loadtxt(positions_file_path)  
# Read data from files

velocity_file_path = "Data/B_J1/Velocity/frame_1000.dat"
magnitudes = np.loadtxt(velocity_file_path)
  # Assuming magnitudes_file.txt contains u, v magnitudes

# Extract x, y positions from the positions data
x_positions = positions[:, 0]
y_positions = positions[:, 1]

# Extract u, v magnitudes from the magnitudes data
u_magnitudes = magnitudes[:, 0]
v_magnitudes = magnitudes[:, 1]

# Plotting Vector Field with QUIVER
plt.quiver(x_positions, y_positions, u_magnitudes, v_magnitudes, color='g')
plt.title('Vector Field')

# Setting x, y boundary limits
plt.xlim(np.min(x_positions) - 1, np.max(x_positions) + 1)
plt.ylim(np.min(y_positions) - 1, np.max(y_positions) + 1)

# Show plot with grid
plt.grid()
plt.show()