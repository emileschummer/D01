

import numpy as np
import matplotlib.pyplot as plt
import os

# Get the current directory of the script
current_dir = os.getcwd()
# Step 1: Read data from "XY.dat" file
print(current_dir)

xy_data_path = os.path.join(current_dir,'Data','B_J1','XY.dat')
xy_data = np.loadtxt(xy_data_path)
X = xy_data[:, 0]  # X coordinates
Y = xy_data[:, 1]  # Y coordinates
sizeofXY=len(X)
i=np.arange(1,sizeofXY+1)

for numeber in i:
    # Step 2: Read velocity data from "velocity.dat" file
    velocity_data_path = os.path.join(current_dir,'Data','B_J1','Velocity',f'frame_{numeber}.dat')
    velocity_data = np.loadtxt(velocity_data_path)
    Vx = velocity_data[:, 0]  # Velocity in X direction
    Vy = velocity_data[:, 1]  # Velocity in Y direction
    Vx = Vx
    Vy = Vy

    # Step 3: Create meshgrid for vector field

    x_min, x_max = np.min(X)-1, np.max(X)+1
    y_min, y_max = np.min(Y)-1, np.max(Y)+1
    print(x_max,x_min,y_max,y_min)


    #x_range = np.linspace(x_min, x_max, 20)
    #y_range = np.linspace(y_min, y_max, 20)
    #print(x_range, y_range)
    #X_grid, Y_grid = np.meshgrid(x_range, y_range)
    #print(X_grid,"NEXT",Y_grid)

    # Step 4: Plot the velocity vector field
    #plt.figure(figsize=(8, 6))
    quiver = plt.quiver(X, Y, Vx, Vy, scale=None)
    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.title('Velocity Vector Field')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.grid(True)
    #plt.show()
    #savename = f"{numeber}_vector_field.png"
    #savedir= os.path.join(current_dir,'first300vectorfieldspngs')
    #plt.savefig(os.path.join(savedir,savename))
    plt.clf()
    offsets = quiver.get_offsets().T  # Get the (x, y) coordinates of the starting points of vectors
    rows, columns = offsets.shape
    print(rows, columns)
