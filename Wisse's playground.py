import random
from scipy import interpolate as inp


def generate_grid_points(rows, cols):
    grid_points = []
    for i in range(rows):
        for j in range(cols):
            grid_points.append((i, j))
    return grid_points

rows = 5  # Number of rows in the grid
cols = 4  # Number of columns in the grid

grid_points = generate_grid_points(rows, cols)
print("Grid points in ascending order:")
for point in grid_points:
    print(point)
    


def generate_random_values(num_values):
    random_values = [random.random() for _ in range(num_values)]
    return random_values

rows = 5  # Number of rows in the grid
cols = 4  # Number of columns in the grid

grid_points = generate_grid_points(rows, cols)
num_points = len(grid_points)

random_values = generate_random_values(num_points)

sorted_indices = sorted(range(len(grid_points)), key=lambda k: grid_points[k])
sorted_grid_points = [grid_points[i] for i in sorted_indices]
sorted_random_values = [random_values[i] for i in sorted_indices]

print("Grid points in ascending order with corresponding random values:")
for point, value in zip(sorted_grid_points, sorted_random_values):
    print(f"Point: {point}, Value: {value}")

interpolator = inp.RegularGridInterpolator(sorted_grid_points, sorted_random_values, method='linear')