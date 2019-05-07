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
Count the kmers of size k
"""
def count_kmers (k,seq):
    kmers = {}
    total_kmers  = 0 # all possible kmers
    count = 0 # all observed kmers

    # for every vale of (1,2, ..., k)
    for i in range(k)
        # calculate the number of kmers for length k
        for char in seq:
            
    create_df(kmers)
    make_graph(kmers,count)
    complexity(count,total_kmers)
    return
"""
"""
def create_df ():
    #count_kmers (k)
    return
"""
Create a graph to show the observed kmers
"""
def make_graph (kmers):
    return
"""
Linguistic complexity of the given sequence
"""
def complexity (observed,possible):
    return (observed/possible)*100
"""
Testing script for the program
"""
def _test ():
    return
"""
Extract sequence, remove endline characters from file
"""
def _strip (file):
    return sequence

def __main__ ():
    sys.argv()
    file = open(filename)
    sequence = _strip(file)
    """
    print("")
    print("")
    print("      ---------------------------------------------------------")
    k = int(input("       Enter the value for k: "))
    """
    count_kmers(k,sequence)
    return

# let's run this
__main__()
