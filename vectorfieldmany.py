import os
from vectorfieldfun import vectorfieldpng
import time

data_directory = "Data/B_J1/Velocity"

#function that makes pngs of a large amount of frames input the start and end frame
def vectorfieldmany(start_frame, end_frame):
    # Iterate over frame numbers
    frame_number = start_frame  # Start with the first frame
    while True:
        # Construct the file path for the current frame
        file_path = os.path.join(data_directory, f"frame_{frame_number}.dat")
        
        # Call the vectorfieldpng function for the current frame
        vectorfieldpng(file_path, frame_number)
        
        # Increment frame number
        frame_number += 1
        if frame_number>end_frame:
            break
        
        
        
        # Check if the next file exists
        next_file_path = os.path.join(data_directory, f"frame_{frame_number}.dat")
        if not os.path.exists(next_file_path):
            break  # Exit the loop if the next file doesn't exist