"""
1. Define a function to count kmers of size k, where k is specified as an argument.
2. Define a function to create a pandas data frame containing all possible k and the associated
number of observed and expected kmers (see above table).
3. Define a function to produce a graph from the data frame of the proportion of each kmer
observed.
4. Define a function to calculate linguistic complexity.
5. Write a script to thoroughly test each of your functions.
6. Use the main function to read in your sequence data and output results.
7. Create a github repository including a README (in markdown) to submit your work. Be sure that
all your functions have appropriate docstrings.
"""

"""
"""
def count_kmers (k):
    kmers = []
    poss  = 0 # all possible kmers
    count = 0 # all observed kmers

    # iterate the sequence and find unique substrings in k
    for i in range(len(sequence)):
        while (len(sequence)-k):
            
    # s
    #
    return
"""
"""
def create_df ():
    #count_kmers (k)
    return
"""
"""
def make_graph ():
    return
"""
Linguistic complexity of the given sequence
"""
def calc_lc (observed,possible):
    return (observed/possible)*100

def _test ():
    return

def _strip ():
    return

def __main__ ():
    sys.argv()
    file = open(filename)
    _strip(file)
    return

# let's run this
__main__()
