import pandas as pp

def count_kmers (k,genome,length):
    """
    Summary -- Count the kmers of size k in a given sequence

    Description -- Determine all of the possible kmers of size k for a given sequence. Record and count all of the unique (observed) kmers for the sequence.

    Parameters:
        - k: size of the the subsets
        - genome: sequence given by the user through the command line
        - length: length of the genome sequence

    Returns -- A tuple of the unique kmers that were found for the specifed k. The first value of the tuple is the total possible kmers for size k and the second value is a list of unique kmers of size k. The number of observed kmers is obtained by taking the length of this list.
    """
    sequences = []
    count = 0 # all observed kmers

    for i in range(length):
        if length < (i+k):
            break # exit loop if you are on element lenghth-k
        # if value of the k is equal to the size of the sequence
        if length == k:
            sequences.append(genome)
            k_kmers = (1,sequences)
            return k_kmers
        # if k is smaller than the length of the sequence
        else:
            seq = genome[i:i+k]
            if seq not in sequences:
                sequences.append(seq)
            count += 1
    if k == 1:
        count = 4
    return (count,sequences)


def create_df (k,genome):
    """
    Summary -- Create a data frame containing all kmers

    Description -- Find all of the possible kmers (observed and possible) for values of k {1,...,k} in a given genome sequence.

    Parameters:
        - k: given as an agrument from the command line, size of the the subsets
        - genome: sequence given as an argument from the command line

    Returns -- Complete dictionary of kmers
    """
    length = len(genome)
    kmers = {}

    # for every value of k inclusive (1,2, ..., k)
    for i in range(1,k+1):
        k_kmers = count_kmers(i,genome,length)
        kmers[i] = k_kmers

    kmers_df = pp.DataFrame.from_dict(kmers,orient = 'index')
    return kmers

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
    return int(observed/possible)*100,observed,possible

def _extract_sequence (file):
    """
    Summary -- Testing script for the program

    Description --

    Parameters:

    Returns -- Nothing
    """
    return sequence
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

    k = 9
    i = 1
    ans = {1:(4, ['A', 'T', 'G']),2:(8, ['AT', 'TT', 'TG', 'GG', 'GA']),3:(7, ['ATT', 'TTT', 'TTG', 'TGG', 'GGA', 'GAT']),4:(6, ['ATTT', 'TTTG', 'TTGG', 'TGGA', 'GGAT', 'GATT']),5:(5, ['ATTTG', 'TTTGG', 'TTGGA', 'TGGAT', 'GGATT']),6:(4, ['ATTTGG', 'TTTGGA', 'TTGGAT', 'TGGATT']),7:(3, ['ATTTGGA', 'TTTGGAT', 'TTGGATT']),8:(2, ['ATTTGGAT', 'TTTGGATT']),9:(1, ['ATTTGGATT'])}
    for i in range(k):
        if i != 0:
            print("k: ",i)
            count_kmers(i,'ATTTGGATT',9)
            assert (ans[i]==count_kmers(i,'ATTTGGATT',9))
    return

def __main__ ():
    """
    Summary -- Output the calculations for the linguistic complexity

    Description -- Takes a file from the commandline and a value for k to pass into functions that will calculate the lingustic complexity and create a graph.

    Parameters: None

    Returns -- Nothing
    line.strip(file,":")
    """
    file = sys.argv[1]
    genome = _extract_sequence(file)
    assert (len(genome) > 0) # do not begin computation if the file was empty
    k = int(input("       Enter the value for k: "))
    assert (k > len(genome)) # if k is greater, cannot compute the complexity

    kmers = create_df(k,genome)
    make_graph(kmers)
    complexity,observed,possible = complexity(kmers)

    print("Total observed: ", complexity)
    print("Total no. of kmers possible: ", complexity)
    print("---------------------------------------------------------")
    print("Complexity of the genome is %", complexity)
    print("---------------------------------------------------------")
    return

# let's run this
__main__()
