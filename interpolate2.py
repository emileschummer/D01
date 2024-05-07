import numpy as np
from scipy.interpolate import griddata
import os
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import cm




positions_file_path = f"{'C'}_J{0}/XY.dat"
positions = np.loadtxt(positions_file_path)



data_directory = f"{'C'}_J{0}/Velocity"
    
    

# Construct the file path for the current frame
file_path = os.path.join(data_directory, f"frame_{1}.dat")

# Get velocities
velocities = np.loadtxt(file_path)

# Create lists
u_components = velocities[:, 0]
v_components = velocities[:, 1]  

wall_file_path = f"{'C'}_J{0}/wall.dat"
#Nparray of position
wall_positions = np.loadtxt(wall_file_path)


'''


# Create a dense grid
grid_x, grid_y = np.meshgrid(
    np.linspace(min(x.min(), x_wall.min()), max(x.max(), x_wall.max()), 764),
    np.linspace(min(y.min(), y_wall.min()), max(y.max(), y_wall.max()), 216)
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
plt.show()'''



import numpy as np
from scipy.interpolate import griddata

# Sample data: replace these with your actual data arrays
existing_points = np.array(positions)  # Existing (x, y) points
existing_u = np.array(u_components)                  # u components at existing points
existing_v = np.array(v_components)                  # v components at existing points
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
    return griddata(points, values, new_points, method='cubic')

# Interpolate u and v components
new_u = interpolate_velocities(all_points, all_u, new_points)
new_v = interpolate_velocities(all_points, all_v, new_points)
# Example of handling NaNs by setting them to zero or another appropriate value
new_u = np.nan_to_num(new_u, nan=0)
new_v = np.nan_to_num(new_v, nan=0)

total_pos=np.vstack((positions, new_points))
total_u=np.hstack((u_components,new_u))
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
import numpy as np
from scipy.interpolate import griddata

# Sample data with a slight modification to avoid perfect alignment
existing_points = np.array([[1, 1], [2, 2], [3, 3]])
existing_u = np.array([10, 20, 30])
existing_v = np.array([15, 25, 35])
wall_points = np.array([[1.5, 1.6], [2.5, 2.6], [3.5, 3.6]])  # Slight offset to avoid perfect alignment

def generate_intermediate_points(existing_points, wall_points, num_points=5):
    all_inter_points = []
    for ep, wp in zip(existing_points, wall_points):
        for t in np.linspace(0, 1, num_points + 2)[1:-1]:
            inter_point = ep * (1 - t) + wp * t
            all_inter_points.append(inter_point)
    return np.array(all_inter_points)

new_points = generate_intermediate_points(existing_points, wall_points)

all_points = np.vstack([existing_points, wall_points])
all_u = np.concatenate([existing_u, np.zeros(len(wall_points))])
all_v = np.concatenate([existing_v, np.zeros(len(wall_points))])

def interpolate_velocities(points, values, new_points, method='linear'):
    return griddata(points, values, new_points, method=method)

new_u = interpolate_velocities(all_points, all_u, new_points)
new_v = interpolate_velocities(all_points, all_v, new_points)

print("New Points:", new_points)
print("Interpolated U:", new_u)
print("Interpolated V:", new_v)
'''