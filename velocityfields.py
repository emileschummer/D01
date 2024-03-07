import numpy as np
import matplotlib.pyplot as plt
import os

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Step 1: Read data from "XY.dat" file

xy_data_path = os.path.join(current_dir,'Data','B_J1','XY.dat')
xy_data = np.loadtxt(xy_data_path)[:400]
X = xy_data[:, 0]  # X coordinates
Y = xy_data[:, 1]  # Y coordinates

# Step 2: Read velocity data from "velocity.dat" file
velocity_data_path = os.path.join(current_dir,'Data','B_J1','Velocity','frame_1.dat')
velocity_data = np.loadtxt(velocity_data_path)[:400]
Vx = velocity_data[:, 0]  # Velocity in X direction
Vy = velocity_data[:, 1]  # Velocity in Y direction
Vx = Vx/3
Vy = Vy/3

# Step 3: Create meshgrid for vector field

x_min, x_max = np.min(X), np.max(X)
print(x_min, x_max)

y_min, y_max = np.min(Y), np.max(Y)
print(y_min, y_max)


x_range = np.linspace(x_min, x_max, 20)
y_range = np.linspace(y_min, y_max, 20)
#print(x_range, y_range)
X_grid, Y_grid = np.meshgrid(x_range, y_range)
#print(X_grid,"NEXT",Y_grid)

# Step 4: Plot the velocity vector field
plt.figure(figsize=(8, 6))
plt.quiver(X_grid, Y_grid, Vx, Vy, scale=20)
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.title('Velocity Vector Field')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.grid(True)
plt.show()
