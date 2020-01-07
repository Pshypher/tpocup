# count poker hands

# 1. open the poker data file for reading
def open_file():
    '''Opens and return the poker file whose probability for each hand rank
        is to be determined. Re-prompts the user for an input if a wrong file
        name is entered.'''
    file_str = input("Enter a file name: ")
    while True:     # loop until you break
        try:
            poker_file = open(file_str, 'r')
            break                   # success! so move on to rest of program
        except IOError:
            print("Error opening file:", file_str)
            file_str = input("Enter a file name: ")
    
    return poker_file

def count_hand_ranks(poker_file):
    '''Counts each hand rank 0-9 and the total number of lines in the
        file object <poker_file>. Returns a tuple.'''
    
    # all counts are ints, so count as a suffix is enough
    total_count = 0
    hand_ranks = [0 for i in range(10)] # Initialize the count for each hand
                                        # rank as 0s in a list of ints

    for line_str in poker_file:
        total_count = total_count + 1
        fields = line_str.split(',')            # split on a comma
        hand_rank_str = fields[-1]              # and get the last field
        try:
            hand_rank_int = int(hand_rank_str)
        except ValueError:
            continue                # bad line: quietly skip this line of the file
        # Update each index of the hand_ranks list based on the value of the
        # hand in each line
        hand_ranks[hand_rank_int] += 1
        
    return total_count,hand_ranks


poker_file = open_file()
total_count, hand_ranks = count_hand_ranks(poker_file)

# Display results
print("Total hands in file: ", total_count)
print("Hand counts by rank number: ", hand_ranks[0], hand_ranks[1], hand_ranks[2], \
      hand_ranks[3], hand_ranks[4], hand_ranks[5], hand_ranks[6], \
      hand_ranks[7], hand_ranks[8], hand_ranks[9])

print("Probability:")
print(" of nothing:         {:>9.4%}".format(hand_ranks[0]/total_count))
print(" of one pair:        {:>9.4%}".format(hand_ranks[1]/total_count))
print(" of two pairs:       {:>9.4%}".format(hand_ranks[2]/total_count))
print(" of three of a kind: {:>9.4%}".format(hand_ranks[3]/total_count))
print(" of a straight:      {:>9.4%}".format(hand_ranks[4]/total_count))
print(" of a flush:         {:>9.4%}".format(hand_ranks[5]/total_count))
print(" of a full house:    {:>9.4%}".format(hand_ranks[6]/total_count))
print(" of four of a kind:  {:>9.4%}".format(hand_ranks[7]/total_count))
print(" of a straight flush:{:>9.4%}".format(hand_ranks[8]/total_count))
print(" of a royal flush:   {:>9.4%}".format(hand_ranks[9]/total_count))