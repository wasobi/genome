import pandas as pp
import math

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

def count_kmers (k,genome,length):
    """
    Summary -- Count the kmers of size k in a given sequence

    Description -- Determine all of the possible kmers of size k for a given sequence. Record and count all of the unique (observed) kmers for the sequence.

    Parameters:
        - k: size of the the subsets
        - genome: sequence given by the user through the command line
        - length: length of the genome sequence

    Returns -- Nothing A dictionary of the unique kmers that were found for the specifed k. The key is the total number of kmers that are possible
    """
    sequences = []
    count = 0 # all observed kmers
    k_kmers = (count,sequences) # empty tuple

        for i in range(length-k):
            if length < (i+k):
                break # exit loop if you are on element lenghth-k
            # if value of the k is equal to the size of the sequence
            if length == k:
                sequences.append(genome)
                k_kmers = (1,sequence)
                return k_kmers
            # if k is smaller than the length of the sequence
            else:
                seq = genome[i:i+k]
                if seq not in sequences:
                    sequences.append(seq)
            count += 1 # incremented at every iteration
    return k_kmers


def create_df (k,genome):
    """
    Summary -- Create a data frame containing all kmers

    Description -- Find all of the possible kmers (observed and possible) for values of k {1,...,k} in a given genome sequence.

    Parameters:
        - k: given as an agrument from the command line, size of the the subsets
        - genome: sequence given as an argument from the command line

    Returns -- Nothing
    """
    length = len(genome)
    kmers = {}

    # for every value of k inclusive (1,2, ..., k)
    for i in range(k):
        k_kmers = count_kmers(k,seq,length)
        kmers[i] = k_kmers

    kmers_df = pd.DataFrame.from_dict(kmers,orient = 'index', columns = [''])
    return observed,possible

def make_graph (kmers,count):
    """
    Summary -- Create a graph to show the observed kmers

    Description --

    Parameters:

    Returns -- Nothing
    """
    return

def complexity (kmers):
    """
    Summary -- Linguistic complexity of the given sequence

    Description -- Takes a sum of all the observed kmers and the sum of all the possible kmers to calculate the linguistic complexity from a dictionary of kmers.

    Parameters:
        - dictionary of all kmers found for the sequence

    Returns -- The percentage of complexity that has been calculated for the sequence.
    """
    observed = 0
    possible = 0
    for k_kmer in kmers:
        observed += len(kmers[k_kmer][1])
        possible += kmers[k_kmer][0]
    return int(observed/possible)*100


def _test ():
    """
    Summary -- Testing script for the program

    Description --

    Parameters:

    Returns -- Nothing
    """
    k = 6
    kmers = {1:(4,['A','T','C','G']),2:(5,['AA','AT','TG','GC','CT']),3:(4,['AAT','ATG','TGC','GCT']),4:(3,['AATG','ATGC','TGCT']),5:(2,['AATGC','ATGCT']),6:(1,['AATGCT'])}
    observed = 16
    possible = 16
    complexity = 100
    return

def __main__ ():
    """
    Summary -- Takes a file from the commandline

    Description --

    Parameters:

    Returns -- Nothing
    """
    sys.argv()
    file = open(filename)
    sequence = line.strip(file,":")

    assert (len(sequence) > 0) # do not begin computation if the file was empty
    k = int(input("       Enter the value for k: "))
    assert (k > len_sequence) # if k is greater, cannot compute the complexity

    kmers = create_df(k,genome)
    make_graph(kmers)
    complexity = complexity(kmers)

    print("---------------------------------------------------------")
    print("Complexity of the genome is %", int(observed/possible)*100)
    print("---------------------------------------------------------")
    return

# let's run this
__main__()
