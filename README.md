# Genome
## Description
Python script created for DSP 439 that calculates the linguistic complexity for a given genome sequence using a value of k that is specified by the user.
## Background

The genome of an organism consists of a very long sequence of nucleic acids. From a computational perspective, this can be thought of as a long string of letters where the alphabet consists only of A, C, G, and T (e.g. ATGTCTGTCTGTA). This string can be divided into a substring of length k, where the possible number of substrings of length k (termed k-mers) is 4^k. The linguistic complexity of the string is defined as the proportion of k-mers that are observed compared to the total number that are theoretically possible. The linguistic complexity of genomes affects genome assembly, can be used to estimate genome size, and allows bacterial species to be identified (if you're not a biologist you don't need to worry about this part).
Write a script that, when run using the command line, outputs the linguistic complexity of each sequence in a file of sequences. The file should be specified by the end user as a command line argument.


As an example, consider the sequence ATTTGGATT. From the following table you can see that the linguistic complexity is 35 / 40 = 0.875. Note that the possible number of kmers (usually 4^k) is limited by the length of the sequence (i.e. the number of possible k-mers of length 9 in the sequence is 1, not 4^9).
