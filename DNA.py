#  File: DNA.py

#  Description: A list of DNA sequences will be given in a file to compare.
#  The program will compare 2 sequences at a time and list out the longest common sequences in alphabetical order.

#  Student Name: Vaishnavi Sathiyamoorthy

#  Student UT EID: vs25229

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 08/23/2022

#  Date Last Modified: 08/25/2022

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.




#  This function takes 2 sequences, converts them to uppercase letters, determines the shorter and longer sequence,
#  and returns the sequences that are common between the two sequences

import sys
# sys.standardinput.readline
# sys.stdin.readline()
def longest_subsequence (s1, s2):
    #  converting to uppercase
    s1 = s1.upper()
    s2 = s2.upper()

    #  determining the longer and shorter sequence
    shorter_sequence = s1
    longer_sequence = s2
    if (len(s1) > len(s2)):
        shorter_sequence = s1
        longer_sequence = s2
    else:
        shorter_sequence = s2
        longer_sequence = s1

    #  An empty list of the common long sequences are created
    #  The length variable determines how many of the nucleic acids are being compared at once.
    common_long_sequences = []
    length = 2
    #  As long as the length variable is not longer than the sequence, this while loop will keep running.
    while (length <= len(shorter_sequence)):
        #  Another function is called so that each of the lengths are compared to find common sequences between the two.
        #  If the function returns 1 or more sequences, those sequences will be assigned to common_long_sequences.
        if (len(common_sequence(shorter_sequence, longer_sequence, length)) != 0):
            common_long_sequences = common_sequence(shorter_sequence, longer_sequence, length)
        length += 1

    #  The initial if else statement determines whether to return the variable common_long_sequences or to return "No common sequences found"
    if (len(common_long_sequences) != 0):
        if_duplicates = []

        #  This for loop makes sure that there are not duplicates of the common sequences
        for i in range(len(common_long_sequences)):
            if(common_long_sequences[i] not in if_duplicates):
                if_duplicates.append(common_long_sequences[i])
        common_long_sequences = if_duplicates
        #  common_long_sequences is sorted so that the sequences are returned in alphabetical order.
        common_long_sequences = sorted(common_long_sequences)
        for i in range(len(common_long_sequences) - 1):
            print(common_long_sequences[i])
        return common_long_sequences[len(common_long_sequences) - 1]
    else:
        return "No Common Sequence Found"
        
           
#  This function takes in the parameters of the shorter sequences, longer sequence, and the length.
#  This function will only work if the first sequence is less than or equal to in length as the second parameter.
def common_sequence(shorter, longer, length):
    #  An empty list of common sequences is made
    common_sequences = []

    #  The outer loop goes through the shorter sequence and the inner loop goes through the longer sequence.
    #  Subsequences are compared from the inner and outer loop. If there is a common sequence, the sequence as added to the list of common_sequences.
    #  The common sequences are returned.
    for i in range((len(shorter) - (length) + 1)):
        end = i + length
        sequence_1 = shorter[i:end]
        for j in range((len(longer) - (length) + 1)):
            end = j + length
            sequence_2 = longer[j:end]
            if (sequence_1 == sequence_2):
                common_sequences.append(sequence_1)
    return common_sequences

#  The file is opened. The first line contains the number of DNA pairs. That is how many times the for loop runs.
#  The longest_subsequence function is called to determined the longest subsequence for each pair of DNA sequences.
#  Every time the .readline() is called, the next line is read.
def main():
    dna_file = sys.stdin
    total_comparisons = int(dna_file.readline().strip())
    for i in range(total_comparisons):
        print(longest_subsequence(dna_file.readline().strip(), dna_file.readline().strip()))
        print()

#  The main function is called.
if __name__ == "__main__":
    main()
