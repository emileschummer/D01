
def loadbin(bin,plane, J_number):
    import numpy as np 
    #load data
    path_bins = f"{plane}_J{J_number}/Binning/binds.dat"
    path_counts = f"{plane}_J{J_number}//Binning/counts.dat"

    # Load the bins
    bins = np.loadtxt(path_bins)
    # Load the counts
    counts = np.loadtxt(path_counts)
    
    index_dict = {}  # Dictionary to store indexes
    
    # Iterate through the big list and populate the index dictionary
    for i, num in enumerate(bins):
        if num not in index_dict:
            index_dict[num] = [i]
        else:
            index_dict[num].append(i)

    
    # Retrieve the list corresponding to the given bin value
    if bin in index_dict:
        return index_dict[bin]
    else:
        return []
            
