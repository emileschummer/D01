
def loadbin(bin):
    import numpy as np 
    print('pizza')
    path_bins = 'Data/B_J1/Binning/binds.dat'
    path_counts = 'Data/B_J1/Binning/counts.dat'

    # Load the bins
    bins = np.loadtxt(path_bins)
    # Load the counts
    counts = np.loadtxt(path_counts)
    print('pizza')
    index_dict = {}  # Dictionary to store indexes
    print('pizza')
    # Iterate through the big list and populate the index dictionary
    for i, num in enumerate(bins):
        if num not in index_dict:
            index_dict[num] = [i]
        else:
            index_dict[num].append(i)

    print('pizza')
    # Retrieve the list corresponding to the given bin value
    if bin in index_dict:
        return index_dict[bin]
    else:
        return []
            
