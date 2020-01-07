# Calculates the passer rating of a Quarterback.
# requires five inputs: pass completions, pass attempts, total passing yards,
# touchdown passes and interceptions.

pass_attempts_str = input("Quarterback pass attempts: ")
pass_attempts_int = int(pass_attempts_str)
pass_completions_str = input("Quarterback pass completions: ")
pass_completions_int = int(pass_completions_str)
total_passing_yards_str = input("Total passing yards: ")
total_passing_yards_float = float(total_passing_yards_str)
touchdowns_str = input("Touchdowns: ")
touchdowns_int = int(touchdowns_str)
interceptions_str = input("Total interceptions: ")
interceptions_int = int(interceptions_str)

# C is the "completions per pass attempt" times 100 minus 30, all divided by 20.
# Y is the "yards per pass attempt" minus 3, all divided by 4
# T is the "touchdown per pass attempt" times 20.
# I the "interceptions per pass attempt"

C = (pass_completions_int / pass_attempts_int * 100 - 30) / 20
Y = (total_passing_yards_float / pass_attempts_int - 3) / 4
T = touchdown_passes_int / pass_attempts_int * 20
I = 2.375 - (interceptions_int / pass_attempts_int * 25)

# The PASSER RATING is computed as the summ of C, Y, T and I all divided by 6
# and then multiplied 100.
PR = (C + Y + T + I) / 6 * 100

print("Completion% {:.3f}, Passing Yards per Attempt {:.3f}, Touchdown Passes% \
 {:.3f} Intercepted Passes% {:.3f} and Quarterback Passer Rating {:.3f}".format(C,Y,T,I,PR))
