from Bin_average_function import bin_average_vector_field
from Bin_average_function import bin_average_vector_field_image
from Bin_average_function import bin_average_velocities
from Vorticity_image_gen import Vorticity_image

u_magnitudes, v_magnitudes = bin_average_velocities(13, 'B', 1)
Vorticity_image(u_magnitudes, v_magnitudes, 'B', 1, 13)