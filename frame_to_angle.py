
import numpy as np

"""

This functions finds to which (angle) bin a certain frame corresponds to
Evey bin is X degrees wide

"""


# 72, 144, 216, 288, 360 - Bin angles for bins = 5
# Everything fits in 5 bins which are separated by 72 degrees4


# Number of bins
bins = 5

# Bin lists
Bin1 = []
Bin2 = []
Bin3 = []
Bin4 = []
Bin5 = []

# Prop configurations
n0 = 0
n1 = 48
n2 = 36

# Sample rate
sample_rate = 15 # Hz

# Placeholder frame number
frame_number = 1
frame = "hello"

# Assign the frame to a bin
if n0 == 0:
    print("No prop")

if n1 == 48: # Frames are in order for the beams frame1 = bin1 and so on...
    rest = frame_number % bins
    if rest == 0:
        Bin5.append(frame)
    elif rest == 1:
        Bin1.append(frame)
    elif rest == 2:
        Bin2.append(frame)
    elif rest == 3:
        Bin3.append(frame)
    elif rest == 4:
        Bin4.append(frame)


if n2 == 36: # Frames skip 1 bin everytime s.t. frame1 = bin2, frame2 = bin4, frame3 = bin1, frame4 = bin3, frame5 = bin5, It's confusing yes
    rest = frame_number % bins
    if rest == 0:
        Bin5.append(frame)
    elif rest == 1:
        Bin2.append(frame)
    elif rest == 2:
        Bin4.append(frame)
    elif rest == 3:
        Bin1.append(frame)
    elif rest == 4:
        Bin3.append(frame)
    
print(Bin1, Bin2, Bin3, Bin4, Bin5)
