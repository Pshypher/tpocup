# Calculates the passer rating of a Quarterback from the file
# "quarterback_data.txt"
# requires five inputs: pass completions, pass attempts, total passing yards,
# touchdown passes and interceptions.

HEADING = 1

input_file = open("quarterback_data.txt", 'r')

player_names_lst = []
passer_ratings_lst = []

# Calculate the passer rating of each player
line_no = 1
for line in input_file:
    if line_no == HEADING:
        line_no += 1
        continue
    else:
        fields_lst = line.split(",")
        
        player_names_lst.append(fields_lst[0])
        
        pass_completions_int = int(fields_lst[1])
        pass_attempts_int = int(fields_lst[2])
        total_passing_yards_flt = float(fields_lst[3])
        touchdown_passes_flt = float(fields_lst[4])
        interceptions_int = int(fields_lst[5])
        
    
        # C is the "completions per pass attempt" times 100 minus 30, all divided by 20.
        # Y is the "yards per pass attempt" minus 3, all divided by 4
        # T is the "touchdown per pass attempt" times 20.
        # I the "interceptions per pass attempt"

        C = ((pass_completions_int / pass_attempts_int) * 100 - 30) / 20
        Y = ((total_passing_yards_flt / pass_attempts_int) - 3) / 4
        T = touchdown_passes_flt / pass_attempts_int * 20
        I = 2.375 - ((interceptions_int / pass_attempts_int) * 25)

        # The PASSER RATING is computed as the sum of C, Y, T and I all divided by 6
        # and then multiplied 100.
        PR = (C + Y + T + I) / 6 * 100
        passer_ratings_lst.append(PR)
        
    line_no += 1

input_file.close()

# The players are ranked in order from best to worst according to their passer
# rating
# selection sort algorithm is used to sort the passer_rating_lst
for i in range(len(passer_ratings_lst)):
    for j in range(i, len(passer_ratings_lst)-1):
        highest_pr_flt, index = passer_ratings_lst[j], j
        
        if passer_ratings_lst[j+1] > passer_ratings_lst[j]:
            highest_pr_flt, index = passer_ratings_lst[j+1], j+1
            
        if passer_ratings_lst[i] < highest_pr_flt:
            passer_ratings_lst[i], passer_ratings_lst[index] = highest_pr_flt, passer_ratings_lst[i]
            player_names_lst[i], player_names_lst[index] = player_names_lst[index], player_names_lst[i] 
            
for i in range(len(passer_ratings_lst)):
    print("{:<18s}: {:.2f}".format(player_names_lst[i], passer_ratings_lst[i]))
    
# Verify the passer rating formula using google